from selenium import webdriver
import selenium
import time
import random

driver=webdriver.Chrome('/Users/naimsassine/Downloads/chromedriver')

#first tab
driver.get('https://www.ulb.be/en/ulb-homepage')


def open_UV(username, password):
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    # Open the website
    text = "Here, let me help!"
    driver.get('https://uv.ulb.ac.be/login/index.php?authCAS=CAS')

    try :
        username_box = driver.find_element_by_name('username')
        # Send password
        username_box.send_keys(username)
        # Find password box
        pass_box = driver.find_element_by_name('password')
        # Send password
        pass_box.send_keys(password)
        # Find login button
        login_button = driver.find_element_by_name('submit')
        # Click login
        login_button.click()
    except selenium.common.exceptions.NoSuchElementException:
        print("Already signed in!.")



    time.sleep(3)
    driver.get('https://uv.ulb.ac.be/my/index.php')
    return text

def open_gehol(username, password):
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    # Open the website
    text = "Here, let me help!"
    driver.get('https://sso-cas.ulb.ac.be/cas/login?service=https%3A%2F%2Fgehol.ulb.ac.be%2Fgehol%2Fintranet_login.php%3Faction%3DcasAuth')

    try :
        username_box = driver.find_element_by_name('username')
        # Send password
        username_box.send_keys(username)
        # Find password box
        pass_box = driver.find_element_by_name('password')
        # Send password
        pass_box.send_keys(password)
        # Find login button
        login_button = driver.find_element_by_name('submit')
        # Click login
        login_button.click()
    except selenium.common.exceptions.NoSuchElementException:
        print("Already signed in!.")

    return text



def show_grades(username, password):
    driver.execute_script("window.open('about:blank', 'tab3');")
    driver.switch_to.window("tab3")
    driver.get('http://monulb.ulb.be/')
    text = "Here, let me help!"

    try :
        username_box = driver.find_element_by_name('username')
        # Send password
        username_box.send_keys(username)
        # Find password box
        pass_box = driver.find_element_by_name('password')
        # Send password
        pass_box.send_keys(password)
        # Find login button
        login_button = driver.find_element_by_name('submit')
        # Click login
        login_button.click()
    except selenium.common.exceptions.NoSuchElementException:
        print("Already signed in!.")


    time.sleep(3)
    driver.get('https://monulb.ulb.be/group/student-site/mes-notes')
    return text


def get_more_info():
    text = """Founded in 1834 by Pierre-Théodore Verhaegen, the Free University of Brussels,
    abbreviated ULB, is a French-speaking private research university in Brussels, Belgium.

    ULB is one of two institutions which trace their origins to the Free University of Brussels,
    founded in 1834 by Belgian lawyer Pierre-Théodore Verhaegen. This split along linguistic lines in 1969
    into the French-speaking ULB and Dutch-speaking Vrije Universiteit Brussel (VUB), both founded in 1970.
    It is one of the most important Belgian universities. A major research center open to Europe and the world,
    it has about 24,200 students, 33% of whom come from abroad, and an equally cosmopolitan staff.

    It's current rector is Yvon Englert, and it has 3 main campuses :
    - Solbosch campus, on the territories of Brussels and Ixelles municipalities in the Brussels-Capital Region
    - Plaine campus in Ixelles
    - Erasmus campus in Anderlecht
    """
    return(text)


def studies_information():
    text = """ The ULB has over 40 different Bachelor Majors, 150 Masters, 23 of them
    whom are fully taught in English.

    The academic year normally starts in September, ends in June and is divided into two different
    semesters.

    There are a lot more information on this subject! I would suggest you go visit the websites below to get more details !

    - For more info : https://www.ulb.be/fr/etudier
    - To enroll into studies : https://www.ulb.be/fr/inscriptions
    - To discover the different Bachelors and Masters at the ULB : https://www.ulb.be/servlet/search?page=&l=1&RH=1571625035978711&beanKey=beanKeyRechercheFormation&q=


    """
    return text


def erasmums_information():
    text = """ Here! let me open a page where you will find
    all the necessary information about going or coming abroad!
    Being an erasmus student is really an amazing experience!
    """
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://www.ulb.be/fr/etudier/partir-ou-venir-en-echange')


    return text

def application_information():
    text = """ The applications for the next semester are not closed yet!
    Here, let me open for you the main page of applications, so you could
    get a look at the main steps to take for you to apply!
    """
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://www.ulb.be/fr/inscriptions')


    return text

def phd_information():
    text = """ The ULB is proud to have a honorable list of notable alumnis and many Nobel prices.
    You could be next! A perfect way to introduce yourself to the world of research
    is by doing a PHD.
    Let me help you by giving you first of all a list of all the notable alunmis,
    and afterwards, let me open a page for you that will contain all the informations
    concerning PHDs and doctorats.
    Henri La Fontaine (1854–1943): Nobel Prize for Peace in 1913.
    Jules Bordet (1870–1961): Nobel Prize in Physiology or Medicine in 1919.
    Albert Claude (1898–1983): Nobel Prize in Physiology or Medicine in 1974.
    Ilya Prigogine (1917–2003): Nobel Prize in Chemistry in 1977.
    François Englert (born 1932): Nobel Prize in Physics in 2013.
    Denis Mukwege (born 1955): Nobel Prize for Peace in 2018.
    """
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://www.ulb.be/fr/la-recherche')


    return text


def engagement_information():
    text = "Here, this website could help you!"
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://www.ulb.be/fr/l-universite/l-ulb-s-engage')
    return text

def student_life_information():
    text = "Here, this website could help you!"
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://www.ulb.be/en/campus-life')
    return text

def greeting():
    responses = ["Hello I'm SAL!", "Good to see you again", "Hi there, how can I help"]
    text = random.choice(responses)
    return text

def howudoin():
    responses = ["I'm Good! Thanks for asking", "Feeling Alive!", "Stuck in quarantine! But it's okay!"]
    text = random.choice(responses)
    return text

def goodbye():
    responses = ["See you!", "Have a nice day", "Bye! Come back again soon."]
    text = random.choice(responses)
    return text

def thanks():
    responses = ["Happy to help!", "Any time!", "My pleasure"]
    text = random.choice(responses)
    return text

def noanswer():
    responses = ["Sorry, can't understand you", "Please give me more info", "Not sure I understand"]
    text = random.choice(responses)
    return text

def options():
    responses = ["Oh sorry, I didn't introduce myself! I am SAL, the ULBChatBot. I can answer questions you have concerning the ULB!", "I can answer different kind of questions that you have concerning the ULB!"]
    text = random.choice(responses)
    return text

def food():
    text = """You can get food at the F ! There are different types of meals you can get there : sandwiches, pasta, pizza and
    the Belgian specialities : Boulettes or Vol-Au-Vent!
    Here let me show you where the F building is at!! """
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://umap.openstreetmap.fr/fr/map/ulb-campus-solbosch_228397#18/50.81293/4.38232')

    return text

