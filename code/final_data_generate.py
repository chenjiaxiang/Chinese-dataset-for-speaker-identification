import json
import os

def instance_process():
	tmp_data_folder = os.path.join(os.path.dirname(os.getcwd()), 'tmp_data')
	name_and_alias_file = os.path.join(os.path.dirname(os.getcwd()), 'origin', 'name_and_alias.txt')
	with open(name_and_alias_file, 'r') as f:
		name_and_alias = [item.strip().split(' ')[1] for item in f.readlines()]

	for data_type in ['train', 'dev', 'test']:
		data_type_file = os.path.join(tmp_data_folder, data_type + '.txt')
		with open(data_type_file, 'r') as f:
			data = f.readlines()
		data_type_list = list()
		for index in range(0, len(data), 23):
			one_instance = dict()

			context = []
			for offset in range(21):
				if offset == 10:
					context.append(data[index+offset].replace('---- center', '').strip())
				else:
					context.append(data[index+offset].strip())

			center_sentence = context[10]

			candidate = dict()
			candidate_line = data[index+21].strip().split(' ')
			candidate_list = eval(''.join(candidate_line[:len(candidate_line)//2]))
			for candidate_index in candidate_list:
				candidate[candidate_index] = name_and_alias[candidate_index]

			speaker_info = data[index+22].strip().split(' ')
			speaker = {int(speaker_info[0]):name_and_alias[int(speaker_info[0])]}

			one_instance['center_sentence'] = center_sentence
			one_instance['context'] = context
			one_instance['candidate'] = candidate
			one_instance['speaker'] = speaker

			data_type_list.append(one_instance)

		with open(os.path.join(os.path.dirname(os.getcwd()), 'final_data', data_type+'.json'), 'w') as f:
			json.dump(data_type_list, f, indent=4, ensure_ascii=False)

def person_info_process():
	name_and_alias_file = os.path.join(os.path.dirname(os.getcwd()), 'origin', 'name_and_alias.txt')
	name_info = []

	with open(name_and_alias_file, 'r') as f:
		data = f.readlines()

	for index, line in enumerate(data):
		one_person = {}
		splited_line = line.strip().split(' ')
		person = splited_line[1]
		alias = [item for item in splited_line[1:]]
		gender = {'1':'M', '0':'F'}[splited_line[0]]

		one_person['index'] = index
		one_person['person'] = person
		one_person['alias'] = alias
		one_person['gender'] = gender

		name_info.append(one_person)

	with open(os.path.join(os.path.dirname(os.getcwd()), 'final_data', 'person_info.json'), 'w') as f:
		json.dump(name_info, f, indent=4, ensure_ascii=False)

def speech_verb_process():
	with open(os.path.join(os.path.dirname(os.getcwd()), 'origin', 'speech_verb.txt'), 'r') as f:
		data = f.readlines()
	speech_verb_list = [item.strip() for item in data]

	with open(os.path.join(os.path.dirname(os.getcwd()), 'final_data', 'speech_verb.json'), 'w') as f:
		json.dump(speech_verb_list, f, indent=4, ensure_ascii=False)

if __name__=='__main__':
	# instance_process()
	# person_info_process()
	speech_verb_process()













