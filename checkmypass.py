import requests
import hashlib
import sys

def request_api_data(Query):
    url = 'https://api.pwnedpasswords.com/range/' + Query
    res = requests.get(url)

    if res.status_code !=200:
        raise("There is something wrong with the API!")
    return res
def get_the_count_of_same_leaked_pass(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
    


def check_password(passwords):
    #checking if the password are in the api requests
    hashed_password = hashlib.sha1(passwords.encode('utf-8')).hexdigest().upper()
    #so we need to convert the password to the sha1 hash and convert it to the upper case 
    #for the api to work
    first_5_character, remaining_char = hashed_password[:5], hashed_password[5:]
    response = request_api_data(first_5_character)
    return get_the_count_of_same_leaked_pass(response,remaining_char)

your_password = input("Enter the passwor to check:")
no_of_same_pass = check_password(your_password)
if no_of_same_pass:
    print(f"this password  {your_password} has been used {no_of_same_pass} times")
    print("You should consider changing your password")
else: 
    print("Your password is safe")


