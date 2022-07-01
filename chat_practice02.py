def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
			for line in f:
				lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		msg = line.split(' ')
		time = msg[0]
		person = msg[1]
		if person == 'Allen':
			if msg[2] == '貼圖':
				allen_sticker_count += 1
			elif msg[2] == '圖片':
				allen_image_count += 1
			else:
				for m in msg[2:]:
					allen_word_count += len(m)
		elif person == 'Viki':
			if msg[2] == '貼圖':
				viki_sticker_count += 1
			elif msg[2] == '圖片':
				viki_image_count += 1
			else:
				for m in msg[2:]:
					viki_word_count += len(m)
	print('allen說了', allen_word_count, '個字')
	print('allen傳了', allen_sticker_count, '個貼圖')
	print('allen傳了', allen_image_count, '張圖片')

	print('viki說了', viki_word_count, '個字')
	print('viki傳了', viki_sticker_count, '個貼圖')
	print('viki傳了', viki_image_count, '張圖片')
	
def main():
	lines = read_file('LINE-Viki.txt')
	convert(lines)
	
main()