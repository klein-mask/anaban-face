#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import cv2
import os
import sys
import glob


class AnabanFace:

	IMAGES_DIR = os.path.abspath(os.path.dirname(__file__)) + '/images/'
	IMAGE_SIZE = (200, 200)
	
	def __init__(self, target_file_name):

		self.target_file_name = target_file_name
		self.bf = cv2.BFMatcher(cv2.NORM_HAMMING)
		self.akaze = cv2.AKAZE_create()


	
	
	# 画像データを取得し、指定サイズにリサイズする
	def get_image_data(self, file_name):
		return cv2.resize((cv2.imread((self.IMAGES_DIR + file_name), cv2.IMREAD_GRAYSCALE)), self.IMAGE_SIZE)


	# 比較
	def compare(self):
		s = '🎁　=== 【 {0} 】 に似ている画像を調べます==================\n'.format(self.get_cast_name_by_image(self.target_file_name))
		print(s)

		(target_kp, target_des) = self.akaze.detectAndCompute(self.get_image_data(self.target_file_name), None)

		#比較画像を全て取得
		#files = os.listdir(self.IMAGES_DIR)
		image_path_list = glob.glob(self.IMAGES_DIR + '/*.png')

		results = []
		for image_path in image_path_list:

			file_name = os.path.split(image_path)[1]

			if file_name != self.target_file_name:
				try:
					(comparing_kp, comparing_des) = self.akaze.detectAndCompute(self.get_image_data(file_name), None)
					matches = self.bf.match(target_des, comparing_des)
					dist = [m.distance for m in matches]
					ret = sum(dist) / len(dist)
				except cv2.error:
					ret = error



				cast_name = self.get_cast_name_by_image(file_name)
				s = '\n😏　{0}の画像（{1}）の値：{2}'.format(cast_name, file_name, ret)
				print(s)

				data = {
					'cast_name': cast_name, 
					'similarity': ret
				}
				
				results.append(data)

		if len(results) >= 1:
			most_similar_data = results[0]

			for r in results:
				if r['similarity'] < most_similar_data['similarity']:
					most_similar_data = r
			
			s = '\n\n🍺【 {0} 】に最も似ている画像は、【 {1} 】です。'.format(self.get_cast_name_by_image(self.target_file_name), most_similar_data['cast_name'])
			print(s)


	def get_cast_name_by_image(self, file_name):
		CONFIG = {
			'kei_a': '田中圭',
			'kei_b': '田中圭',
			'ryusei': '横浜流星',
			'kodai': '浅香航大',
			'naoto': '竹中直人'
		}

		return CONFIG[file_name.split('.')[0]]

if __name__ == "__main__":
	args = sys.argv
	
	if len(args) == 2:
		anaban = AnabanFace(args[1])
		anaban.compare()
