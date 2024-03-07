#using dictionary, list and for loop prepare an exam 
#for some students
#and at the end give a result of their total
#score and the answers to the ones that they

m  ={'maths':'30','english': '20', 
                     'history':'50', 'phys':'60'}
total_grade = 0
#list of loop
answers= []




biology =[
  {"question":"what is biology",
   
   "x":{


    "a":"life",
    "b":"love",
    "c":"claw"
    
    },


    "answer":"a"
   
   },



  {"question":"which is an organ in the body",
   
   "x":{
    "a":"liver",
    "b":"spleen",
    "c":"bile"},
    
    "answer":"a"
   
   },
  {"question":"which of these is part of the digestive system flow",
   "x":{
    "a":"peristalysis",
    "b":"systole",
    "c":"diastole"},
    "answer":"a"
   
   },
  {"question":"what organ controls respiration",
   "x":{
     
    "a":"lungs",
    "b":"lyrynx",
    "c":"nose"},



    "answer":"a"
   
   },
]


biol =[
  {"question":"what is biology",
   
   "x":{
    "a":"life",
    "b":"love",
    "c":"claw"
    
    },
    "answer":"a"
   
   },


]


biol[0]['x']


for i in biology:
  print(  biology[i]["question"]  )


  opt = biology[i]['x']

  if(opt ==None):
    opt= " no options available for this question"

  ans =input(    f'  {opt}   '  )

  if (ans.lower() == i['answer']):
    total_grade =total_grade + 1
  else:
    da={"question":i["question"], "answer":i["x"][i['answer']]}  
    answers.append(da)

total_p = total_grade /  len(biology) *100

print(f"total percentage score = {total_p}%  \n" )

if len(answers) > 0:

  print(f"answers to failed questions: {answers} \n")


#Create a list of dictionaries.
#The keys for the dictionaries are name, 
#school, gender,
  


    

female =[{  "background":"information",

    "Name"  :"Eso",
    "school": "Abk",
    "tribe" : "delta",
    "age"   : "10",
    "gender":  "male",
    "Country":"Christian",
    "Religion" : "Nigeria"

    }, 
    
    
    ]