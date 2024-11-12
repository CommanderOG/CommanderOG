import itertools 
 
def brute_force_passwords(characters, min_length, max_length): 
    for length in range(min_length, max_length + 1): 
        for password in itertools.product(characters, repeat=length): 
            yield ''.join(password) 
 
# Example usage 
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._#@*;:'
with open('pass.txt','w+') as f : 
	for password in brute_force_passwords(characters, 5, 14): 
		f.write(password)
		f.write('\n')

print("Done Done")
     