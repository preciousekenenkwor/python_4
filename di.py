# create a list with 3 dictionaries having keys of sex, name, job
#book =[{' name':'john', 'sex':'female', 'job': 'teacher'},
#{ 'name' : 'eso', 'sex':'male', 'job':'doctor'},
#{ ' name': 'john', 'sex':'male',  'job':'artist'},
#]
#for i in book:
    #m=i['job']
   # print(m)
    #a = input(f"is this your sex? {i['sex']} y / n :")
    #if  a == 'y':
        #print("well done")
         # #else:
        #print("booooo")    
#your  a lecturer in a university and you 
#are asked to prepare exam questions 
#for your students using loop list and dictionary
#prepare the exam questions and give their total 
#score after the exam

book=[  
   
   {'question':'whats a medicine',
     
         "options":{
         
         
         'a':'healthcare',
          'b':'house',
          'c':'home',
          'c': 'market'
         },
          'answer':'a'
          },


          {'question':'whats digital',
           'options':{
           'a':'remote delivery',
           'b':'distance delivery',
           'c':'house delivery',
           'd':'school delivery'
           },

           'answer':'a'
           },

           {'question':'whats is science',
            

            'options':{
            'a':'structure',
             'b':'testing',
             'c':'technology',
             'd':'food'
            },
            
             'answer':'c'
               
           },
        
        
        ]
total_score= 0
failed_q_n_a=[]
for i in book:
    print (       i['question']     )
    print ( i['options'])

    y = input ('pls insert your answer:')

    if (y == i['answer']):
     total_score = total_score + 1 
    else:
    
       m={'question':        i['question'],         'answer':   i['options'][i['answer']]}
       failed_q_n_a.append(m)


print("total score: ")
print(total_score)
print("answers to failed questions")
print(failed_q_n_a)


        
#using  dictionary prepare a pass or 
#identity system where the user will 
#have to insert their exam number and name 
#to be authenticated for the exam


