import hashlib

import requests

'''
using the have 'have I been pawned API' to
track how many times a password has been hacked.
'''


def get_api_data(query_input):
	url = 'https://api.pwnedpasswords.com/range/' + query_input
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'error fetching: {res.status_code}, check and try again')
	return res


def pawned_api_check(password):
	# Hash the password with sha1 algorithm from hashlib
	sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	selected_five, remaining_chars = sha1_password[:5], sha1_password[5:]
	data = get_api_data(selected_five)  # send the first 5 chars to the api
	return get_leaks_count(data, remaining_chars)


# check how many times this password has leaked/hacked
def get_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for item, count in hashes:
		if item == hash_to_check:
			return count
	return 0


def main(password):
	count = pawned_api_check(password)
	if count:
		print(f'{password} was found {count} times... change password')
	else:
		print(f'{password} was not found, all good here')
	return 'completed'


if __name__ == '__main__':
	# check password
	main('password')
