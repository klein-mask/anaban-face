#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import cv2
import os
import sys
import glob


class AnabanFace:

	#IMAGES_DIR = os.path.abspath(os.path.dirname(__file__)) + '/images/'
	IMAGES_DIR = os.path.abspath(os.path.dirname(__file__)) + '/images2/'

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
		s = '\n🎁　=== 【 {0} 】 に似ている画像を調べます\n'.format(Pycolor.YELLOW + self.get_cast_name_by_image(self.target_file_name) + Pycolor.END)
		print(s)

		(target_kp, target_des) = self.akaze.detectAndCompute(self.get_image_data(self.target_file_name), None)

		#比較画像を全て取得
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
			
			s = '\n\n\n🍺　=== 【 {0} 】に最も似ている画像は、【 {1} 】です。'.format(Pycolor.YELLOW + self.get_cast_name_by_image(self.target_file_name) + Pycolor.END, Pycolor.RED + most_similar_data['cast_name'] + Pycolor.END)
			print(s)


	def get_cast_name_by_image(self, file_name):
		CONFIG = {
			'kei_a': '田中圭',
			'kei_b': '田中圭',
			'ryusei': '横浜流星',
			'kodai': '浅香航大',
			'naoto': '竹中直人',
			'nana': '手塚菜奈',
			'shota': '手塚翔太',
			'kuroshima': '黒島沙和',
			'nikaido': '二階堂忍',
			'sanae': '榎本早苗',
			'tamiya': '田宮淳一郎',
			'tokoshima': '床島比呂志',
			'kuzumi': '久住譲',
			'kayo': '児嶋佳世',
			'toshiaki': '児嶋俊明',
			'kimiko': '田宮君子',
			'yoko': '石崎洋子',
			'kenji': '石崎健二',
			'humiyo': '石崎文代',
			'kazuo': '石崎一男',
			'ukita': '浮田啓輔',
			'airi': '妹尾あいり',
			'kakinuma': '柿沼遼',
			'shinii': 'シンイー',
			'kuon': 'クオン',
			'ikubaru': 'イクバル',
			'nishimura': '西村淳',
			'ono': '尾野幹葉',
			'kitagawa': '北川澄香',
			'sora': '北川そら',
			'kinoshita': '木下あかね',
			'masashi': '榎本正志',
			'soichi': '榎本総一',
			'hujii': '藤井淳史',
			'eto': '江藤祐樹',
			'sano': '佐野豪',
			'misato': '赤池美里',
			'goro': '赤池吾朗',
			'sachiko': '赤池幸子',
			'kamiya': '神谷将人',
			'mizuki': '水城洋司',
			'hosokawa': '細川朝男',
			'yomogida': '蓬田蓮太郎',
			'sakuragi': '桜木るり',
			'x': 'インターホンの人物X(エックス)'
		}

		return CONFIG[file_name.split('.')[0]]


class Pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'


if __name__ == "__main__":
	args = sys.argv
	
	if len(args) == 2:
		anaban = AnabanFace(args[1])
		anaban.compare()
