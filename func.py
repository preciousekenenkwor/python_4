# def ekene_three( val, *arg, **kwargs):
#     pass 


#def ekene ():
   #print('evol')



#def ekene_one(anything):
   # pass

#def ekene_two(name, religion):
  #  pass  


#def ekene_three(a):
  #  return a
    

#def ekene_four(a):
  #  return a



#e= ekene_three("goal")
#richie= ekene_three("cheese")
#garuna= ekene_three(3489)
#gareth= ekene_four("salvadore")

#print(f)
#print(richie)

#so create a fuction that takes alist as an argument
# and return a double of the list
#def eso(a):
  #  return a *2
#m = eso('hello precious')
#print(m)

#using function create a function that will 
#take any exam questions and return the student score and 
#answer to failed questions a continuation of our previous topic
biology_question= [{'questions':'whats a goat',
        'pen':{
            'a':'is an animal',
            'b':'human',
            'c':'plastic',
            'd':'laptop'
        },
        'answer':'a'
      
    },
    {'questions':'whats a biology',
     'pen':{
         'a':'book',
         'b':'science',
         'c':'food',
         'd':'man'
         
     },
     'answer':'b'


    },
   {'questions':'whats is organ',
    'pen':{
        'a':'nose',
        'b':'leg',
        'c':'mouth',
        'd':'hand'
    },
       'answer':'a'
   },

    ]



    
physics_question= [{'questions':'whats a physics',
        'pen':{
            'a':'science',
            'b':'human',
            'c':'plastic',
            'd':'laptop'
        },
        'answer':'a'
      
    },
    {'questions':'scalar quantity',
     'pen':{
         'a':'mass and no direction',
         'b':'science',
         'c':'food',
         'd':'man'
         
     },
     'answer':'a'


    },
   {'questions':'whats is newton third law',
    'pen':{
        'a':'action and reaction are equal and opposite',
        'b':'leg',
        'c':'mouth',
        'd':'hand'
    },
       'answer':'a'
   },

    ]





def love( exam):
    total = 0
    failed_score = []
    for i in exam:
        print(i["questions"])
        print(i["pen"])
        y= input('enter the answer: ')
        if (y==i['answer']):
            total = total +1
        else:
            x={'questions': i['questions'],  'answer': i['pen'][i['answer']]}
            failed_score.append(x)
    print('total:')
    print(total)
    print('answer to failed questions')
    print(failed_score)


love(physics_question)    