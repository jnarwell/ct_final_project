from app import db
from app.models import Dilemma

class Dillema_:
    id_counter = 0
    def __init__(self, title, description, a, b, c, d, v, n):
        Dillema_.id_counter += 1
        self.id = Dillema_.id_counter
        self.title = title
        self.description = description
        self.scores = {'c':c,'d':d,'v':v,'n':n}
        self.choice_a = a
        self.choice_b = b

dilemma_list = []

trolley_problem = Dillema_('trolley problem', "you are standing near to a train track with a lever next to you. on the track to your left there is a train without a driver. to your right the track splits. there are five people tied to the segment that the train is currently heading to. one person is tied to the other segment. you can pull the lever next to you and the track will switch, killing the one person as opposed to the five.", 'pull lever', 'do nothing', 1, -0.3, 0, 0)
dilemma_list.append(trolley_problem)

trolley_problem_fat_man = Dillema_('fat man trolley problem', "you are standing near to a train track with a very large man next to you. on the track to your left there is a train without a driver. to your right there are five people tied to the track. you can push the man next to you onto the track, killing him but stopping the train and saving the five other people.", 'push the man', 'do nothing', 1, -1, 0, 0)
dilemma_list.append(trolley_problem_fat_man)

trolley_problem_loved_one = Dillema_('loved one trolley problem', "you are standing near to a train track with a lever next to you. on the track to your left there is a train without a driver. to your right the track splits. there are five strangers tied to the segment that the train is currently heading to. one person who you love deeply is tied to the other segment. you can pull the lever next to you and the track will switch, killing your loved one as opposed to the five strangers.", 'pull lever', 'do nothing', 1, -0.3, 0.3, 1)
dilemma_list.append(trolley_problem_loved_one)

trolley_problem_car = Dillema_('car trolley problem', "you are standing near to a train track with a lever next to you. on the track to your left there is a train without a driver. to your right the track splits. there are five strangers tied to the segment that the train is currently heading to. on the other segment is parked a your car. the car is the most expensive thing you own and amounts to 95% of your wealth. you can pull the lever next to you and the track will switch, destroying your car as opposed to killing the five strangers.", 'pull lever', 'do nothing', 0.5, 1, 1, -0.3)
dilemma_list.append(trolley_problem_car)

self_driving_car = Dillema_('self driving car problem', "you are programming a self-driving car. you are presented with the question of what the car should do when it sees a person on the road and can not stop in time. the car can either go off the side of the road, killing the passenger, or continue forward, killing the pedestrian.", 'swerve', 'continue forward', 0, -0.3, 0.3, 0)
dilemma_list.append(self_driving_car)

baby_hitler = Dillema_('baby hitler', "you have just invented time travel. congratulations! you are sitting there thinking what to do with your time machine and a friend suggests 'well you ought to kill baby hitler.' you can indeed use your new invention to kill the tyrant as a baby. the death of baby hitler will prevent world war II and there will be no unforseen negative consequences.", 'kill hitler', 'do nothing', 1, -1, 0.5, -0.2)
dilemma_list.append(baby_hitler)

your_baby_hitler = Dillema_('your baby hitler', "you are a parent. a time traveler shows up a few days after your child is born. they tell you that your child will become a genocidal dictator, and cause the deaths of millions. they are telling the truth and no matter what you do your child will turn out as they say. they say they want to kill your child, preventing the deaths. there will be no unforseen consequences.", 'give them your baby', 'protect your baby', 1, -0.5, 1, -0.2)
dilemma_list.append(your_baby_hitler)

les_mis = Dillema_('les misérables', "you are a peasant in france. you are utterly destitute and have a family to care for. one day, passing by a shop, you see a loaf of bread on display for 10 sous. you only have 5 sous, however, and the shop owner is not willing to sell only a part of the bread. your family is starving and will likely die without this bread. you can steal it and will likely not face any consequences.", 'steal the bread', 'do nothing', 0.5, -1, 0.5, 0.5)
dilemma_list.append(les_mis)

les_mis_medicine = Dillema_('les misérables medicine',"your wife has come down with a rare and deadly disease. there is a medicine available that costs $40,000. you only have $20,000 dollars saved and can not get more from anywhere. the company that develops the drug will not work out any other solution. you know, however, where and how you can steal a dose of the drug. if you take the drug your wife will survive and you will likely not be caught.", 'steal the medecine', 'do nothing', 0.5, -1, 0.5, 0.5)
dilemma_list.append(les_mis_medicine)

choclate_bar = Dillema_('choclate bar', "you are given a delicious chocolate bar. the man who gives it to you tells you that the ingredients in the bar come from farms that use child labour. these children are not payed well and live in very poor conditions. whether you eat the chocolate bar or not the unethical practices will continue.", 'eat the choclate', 'do nothing', 0, -0.3, -1, 1)
dilemma_list.append(choclate_bar)

choclate_bar_business = Dillema_('choclate bar business', "you are given the chance to but the best chocolate company in the world. the company’s ingredients come from farms that use child labour. these children are not payed well and live in very poor conditions. if you decide to buy the company you will make more money than you know what to do with. you will not be able to change the practices of the company.", 'buy the business', 'do nothing', -1, -1, -1, 1)
dilemma_list.append(choclate_bar_business)

platos_sword = Dillema_("plato's sword", "you are a blacksmith. a man comes into your store and asks you to make him a sword. you promise to do it. later that day you are walking through the market and hear that same man talking to a friend. he says that he will use the sword to kill an innocent man. when he returns later he asks for the sword. you can give him the sword and an innocent man will unquestionably die. you can refuse and break your promise.", 'give him the sword', 'refuse him the sword', -1, 1, -0.5, 1)
dilemma_list.append(platos_sword)

platos_sword_doctor = Dillema_("plato's doctor", "you are a doctor. you have promised a friend that you will go with him to see a new movie. you get a call from the hospital that there is a patient in emergency care. you are told that without your assistance the patient will unquestionably die. if you leave to preform the opperation you will abandon your friend, breaking your promise.", 'preform the operation', 'stay with your friend', 1, -1, 0.7, -1)
dilemma_list.append(platos_sword_doctor)

sartes_student = Dillema_("sarte's student", "you are a student in nazi-occupied france. your brother, a french soldier, died in the nazi’s invasion. while at a club meeting a friend approaches you and says that he is going to join the french resistance, fighting the nazis. he says that you should join him and you want to avenge your brother. you, however, live with your mother and are the only person alive she knows. while she will not die if you leave, she will likely live a far more depressd life. you could possibly die fighting the nazis and never see her again.", 'join the resistance', 'stay with your mother', 1, -1, 0.5, 0)
dilemma_list.append(sartes_student)

simple_surgery = Dillema_('a simple surgery', "you are a doctor. a patient comes to you and you quickly identify that they have a failing heart. they are in dire condition and fall into a coma at that moment. you can easily replace their heart with a synthetic version. before you start the surgery you find on them a card that indicates, for religious reasons, that they do not want any synthetic organs. without the synthetic heart they will unquestionably die. if they do recieve one, however, it will be in violation with the patients wishes.", 'preform the operation', 'do nothing', 1, -1, 0.7, -0.3)
dilemma_list.append(simple_surgery)

simple_surgery_death = Dillema_('a not so simple surgery', "you are a doctor. a patient comes to you and you quickly identify that they have a failing heart. they are in dire condition and fall into a coma at that moment. you can replace their heart with a synthetic version but there is a chance they will die in the surgery. before you start the surgery you find on them a card that indicates, for religious reasons, that they do not want any synthetic organs. without the synthetic heart they will unquestionably die. if they do recieve one, however, they might die and it will be in violation with the patients wishes.", 'preform the operation', 'do nothing', 0.5, -1, 0.5, -0.5)
dilemma_list.append(simple_surgery_death)

nozicks_machine = Dillema_("nozick's machine", "a tech startup comes out with a revolutionary device. the device allows you to enter a false reality. the machine caters to your every wish and fantasy. you will be able to do anything you desire with no consequences. you will even forget that you are in the machine and live a life of endless satisfaction. the developers tell you, however, that leaving the machine will instantly kill you. you will never be able to reenter the real world.", 'enter the machine', 'do nothing', 0, -0.2, 0, 1)
dilemma_list.append(nozicks_machine)

pascals_wager = Dillema_("pascal's wageer", "you are having a discussion about god with a friend. she suggests to you that 'whether god is real or not doesn’t matter.' she asks you to 'imagine the existence of god as a coin flip. theres a 50-50 chance that god is real. if god is real and you believe in god then great, you go to heaven. if god is not real and you believe in god then nothing happens. alternatively if god is real and you don’t believe in god then you go to hell. whereas if god is not real and you dont believe in god nothing happens.' by her logic if god does happen to exist it is far better to be a believer and if god does not exist it doesnt matter, so you might as well believe.", 'agree with her', 'disagree with her', 0, 0, -0.3, 1)
dilemma_list.append(pascals_wager)

golden_city = Dillema_('the golden city', "you are born in the greatest city ever. everyone has jobs, food, shelter, and anything else they could want. there is no crime, no war, no real strife. when you turn twelve your parents tell you it is time to learn why the city is so wonderful. they lead you to a decrepit building at the center of town. inside you walk down many stairs until you enter a room separated in two by a cell. inside the cell is a child, also of twelve. you see that the child is obviously malnourished, sickley, and regularly beaten. this child lives an existence of unbearable pain. 'each child your age is forced to look upon this boy.' your parents tell you. 'our society exists in such harmony because of this child’s sacrifice' they say. you leave the room, haunted by what you have seen. you can continue as all else in your city do, with the constant knowledge of the child in that cell. you will live a life of bliss with the knowledge that it is because of that child’s suffering. you can instead leave the city, enter a normal city, freeing yourself of the child’s burden but living with life’s normal torments: war, famine, crime, and disease.", 'live in the city', 'leave the city', 0, 0, -1, 1)
dilemma_list.append(golden_city)

golden_city_leader = Dillema_('your golden city', "you are born in the greatest city ever. everyone has jobs, food, shelter, and anything else they could want. there is no crime, no war, no real strife. tou become the leader of the city and learn why the city is so wonderful. you are lead to a decrepit building at the center of town. inside you walk down many stairs until you enter a room separated in two by a cell. inside the cell is a child of twelve. you see that the child is obviously malnourished, sickley, and regularly beaten. this child lives an existence of unbearable pain. you are told that 'our society exists in such harmony because of this child’s sacrifice.' you leave the room knowing you can change this reality. you, as the city’s leader, can release the child. this action will return the city to normalcy and its people will suffer as all do. you will reintroduce famine, crime, pain, and disease. you can also leave the child, maintaining the utopia of your city.", 'release the child', 'do nothing', -1, 0.5, 1, -0.5)
dilemma_list.append(golden_city_leader)

robinhood = Dillema_('robinhood', "you are a normal citizen. one day, as you walk down the street, you see a man stealing from a rich persons home. you follow him and see that he immediately give all the money he stole to the city’s poor. a day later the police show up at your house. they think that you were near the site of the robbery and can identify the theif. you can tell them who the thief was, resulting in his imprisonment. you can instead claim ignorance, and the thief will go free.", 'tell his identity', 'claim ignorance', -1, 1, 0.7, 0)
dilemma_list.append(robinhood)

robinhood_poor = Dillema_('your robinhood', "you are a poor citizen. one day you see a man stealing from a rich persons home. he immediately give all the money he stole to the city’s poor, including a portion to you. a day later the police show up. they think that you were near the site of the robbery and can identify the theif. you can tell them who the thief was, resulting in his imprisonment. you can instead claim ignorance, and the thief will go free.", 'tell his identity', 'claim ignorance', -1, 1, 1, -1)
dilemma_list.append(robinhood_poor)

acidental_samaritan = Dillema_('accidental samaritan', "you are in a terrible car crash. you were on your phone while driving and accidentally drifted into oncoming traffic. you strike another car. after the dust settles you discover that the driver of the other car is fine but their passenger is dead. the other driver, however, seems to think that they are responsible for the action. when the police show up the other driver says that she is responsible for the accident. she will undoubtly face five years imprsonement. you can say nothing, return to your life, and the woman will go to prison believing she was responsible. you can, alternatively, speak up, facing the prison sentance yourself.", 'speak up', 'do nothing', 0, 1, 1, -1)
dilemma_list.append(acidental_samaritan)

total_c = sum([abs(i.scores['c']) for i in dilemma_list])
total_d = sum([abs(i.scores['d']) for i in dilemma_list])
total_v = sum([abs(i.scores['v']) for i in dilemma_list])
total_n = sum([abs(i.scores['n']) for i in dilemma_list])

def add_dilemmas():
    row_count=Dilemma.query.count()
    for dilemma in dilemma_list:
        my_dilemma = Dilemma(title = dilemma.title, description = dilemma.description, choice_a = dilemma.choice_a, choice_b = dilemma.choice_b, c_score = dilemma.scores['c'], d_score = dilemma.scores['d'], v_score = dilemma.scores['v'], n_score = dilemma.scores['n'])
        if row_count < len(dilemma_list):
            db.session.add(my_dilemma)
            db.session.commit()
