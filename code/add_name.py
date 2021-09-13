import os

def main():
	origin_data_folder = os.path.join(os.path.dirname(os.getcwd()), 'origin')
	tmp_data_folder = os.path.join(os.path.dirname(os.getcwd()), 'tmp_data')
	name_and_alias_file = os.path.join(origin_data_folder, 'name_and_alias.txt')
	with open(name_and_alias_file, 'r')  as f:
		name_and_alias = [item.strip().split(' ')[1] for item in f.readlines()]
	for data_type in ['train', 'dev', 'test']:
		data_type_file = os.path.join(origin_data_folder, data_type+'.txt')
		with open(data_type_file, 'r') as f:
			data = f.readlines()
		for index in range(len(data)):
			# print(data[index])
			# print(data[index].decode('utf-8'))
			if (index+2)%23 == 0:
				# print(index)
				# print(data[index])
				names = ' '.join([name_and_alias[int(item)-1] for item in eval(data[index].strip())])
				data[index] = data[index].strip() + ' ' + names + '\n'
			if (index+1)%23 == 0:
				# print(index)
				# print(data[index])
				name = name_and_alias[int(data[index].strip())-1]
				data[index] = data[index].strip() + ' ' +  name + '\n'
		with open(os.path.join(tmp_data_folder, data_type+'.txt'), 'w') as f:
			f.writelines(data)
			# for line in data:
				# f.writeline(line)

if __name__=='__main__':
	main() 
