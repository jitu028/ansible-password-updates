import crypt; 

inputfile=open("user_input.txt","r")
outputfile=open("hashed_password.txt","w")

def get_hashed_password(inputfile):

	for line in inputfile.readlines():

		item=line.split()
		server=(item[0])
		user=(item[1])
		read_pass=(item[2])
		hash_pass=crypt.crypt(read_pass, "$6$random_salt")
		#print server
		#print user
		#print read_pass
		#print hash_pass
		outputfile.write(server+"\t"+user+"\t"+(item[2])+"\t"+hash_pass+"\n")
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    #return crypt.crypt(user1ansible, "$6$random_salt")
	
#hash_pass = get_hashed_password("user1ansible")
#print hash_pass

get_hashed_password(inputfile)

	
inputfile.close()
outputfile.close()	