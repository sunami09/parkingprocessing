from tkinter import *
from tkinter import ttk
import customtkinter
import cv2
import cvzone
import pickle
import numpy as np
def show(filename, video, height, width, key, name):
    cap = cv2.VideoCapture(video)
    with open(filename, 'rb') as f:
        posList = pickle.load(f)
    def checkParkingSpace(imgPro):
        spaceCounter = 0

        for pos in posList:
            x, y = pos

            imgCrop = imgPro[y:y + height, x:x + width]
        
            count = cv2.countNonZero(imgCrop)


            if count < key:
                color = (0, 255, 0)
                thickness = 2
                spaceCounter += 1
            else:
                color = (0, 0, 255)
                thickness = 2

            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
            cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,thickness=2, offset=0, colorR=color)

        cvzone.putTextRect(img, f'Parking Lot for ' + name + ':', (250, 22), scale=1, thickness=1, offset=10, colorR=(122, 37, 153))
        cvzone.putTextRect(img, f'Open Spaces Left: {spaceCounter}/{len(posList)}', (250, 52), scale=1, thickness=1, offset=10, colorR=(0,200,0))

    while True:

        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        success, img = cap.read()
        if name == "Costco":
            img = cv2.resize(img, (583, 700))
        elif name == "Trader Joes":
            img = cv2.resize(img, (750, 750))
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        checkParkingSpace(imgDilate)
        cv2.imshow("Image", img)
         # Wait for a key event
        key1 = cv2.waitKey(15)

        # Check if the user clicked the close button
        if key1 == 27 or cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
            # Close the window
            cv2.destroyAllWindows()
            break
    
    
def create_button():
    button = customtkinter.CTkButton(text="Treehacks",master=screen_try, command=lambda: show("CarParkPos", "CarPark.mp4", 47, 107, 950, "Treehacks"), height=50)
    button.place(x=320, y=420)
    
    button = customtkinter.CTkButton(text="Trader Joes",master=screen_try, command=lambda: show("CarParkPos3", "3.mp4", 47, 107, 600, "Trader Joes"), height=50)
    button.place(x=205, y=510)
   
    button = customtkinter.CTkButton(text="Costco Wholesales",master=screen_try, command=lambda: show("CarParkPos5", "5.mp4", 38, 83, 500, "Costco"), height=50)
    button.place(x=435, y=510)
    button = customtkinter.CTkButton(text="Go Back!",master=screen_try, command=mainscreen, height=50)
    button.place(x=320, y=600)
def typeitfirst(widget, index, string):
   if len(string) > 0:
      widget.insert(index, string[0])
      if len(string) > 1:
         # compute index of next char
         index = widget.index("%s + 1 char" % index)

         # type the next character in half a second
         widget.after(50, typeitfirst, widget, index, string[1:])
      else:
          create_button()
    

def try_it_now():
    try:
        screen_more.destroy()
    except:
        pass
    try:
        screen.destroy()
    except:
        pass
    global screen_try
    screen_try = customtkinter.CTk()
    screen_try.iconbitmap("icon2.ico")
    screen_try.geometry("850x700+50+20")
    screen_try.title("Spottr")
    Label(text=" ", bg="#242424", font=("Courier",25)).pack()

    Label(text="Welcome to Spottr!!",bg ="#242424", fg="green",font=("Courier",38,"bold")).pack()
    Label(text=" ", bg="#242424", font=("Courier",25)).pack()
    text = Text(screen_try, bg="#242424", fg="white", font=("times",25))
    text.pack(fill="both", expand=False, padx=20)
    text.config(highlightthickness = 0, borderwidth=0)
    typeitfirst(text, "1.0", "Hey there!👋 I'm Spotti, I'm here to help find stress-free parking, locate open \nspots quickly, and reduce your carbon footprint.\n\nI see you are around Stanford University, these are the three most popular \nplaces people around you often visit:\n1. Treehacks\n2. Trader Joes\n3. Costco Wholesales\nWhere do you want to go today?")
   
    
    
     

    screen_try.mainloop()
def learn_more():
    screen.destroy()
    global screen_more
    screen_more = customtkinter.CTk()
    screen_more.iconbitmap("icon2.ico")
    screen_more.geometry("850x700+50+20")
    screen_more.title("Spottr")
    Label(text=" ", bg="#242424", font=("Courier",65)).pack()
    Label(text="SPOTTR",bg ="#242424", fg="green",font=("Courier",38,"bold")).pack()
    Label(text="", bg="#242424", font=("Courier",12,"bold")).pack()
    Label(text="Introducing the ultimate solution to the parking nightmare - our sustainable and",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    Label(text="cutting-edge parking lot tracker! Our system not only helps drivers navigate through",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    Label(text="parking lots and guides them towards areas with the most available spaces, but also helps",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    Label(text="reduce carbon emissions by saving gasoline.",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    Label(text="", bg="#242424", font=("Courier",7,"bold")).pack()
    Label(text="With real-time information about the busiest parking lots, you can avoid unnecessary",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    Label(text="circling and reduce your carbon footprint. By using our parking lot tracker, you",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    Label(text="are not only making your life easier but also contributing to a greener future.",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    Label(text="", bg="#242424", font=("Courier",7,"bold")).pack()
    Label(text="Say goodbye to parking frustration and hello to a more sustainable and",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    Label(text="eco-friendly way of parking. Our system is the perfect solution for environmentally",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    Label(text="conscious drivers who want to make a positive impact on the planet.",bg ="#242424", fg="white",font=("times",18, "italic")).pack()
    
    button = customtkinter.CTkButton(text="Try it Now!",master=screen_more, command=try_it_now, height=50)
    button.place(x=240, y=470)
    button = customtkinter.CTkButton(text="Go Back!",master=screen_more, command=mainscreen, height=50)
    button.place(x=460, y=470)
    screen_more.mainloop()
    



def mainscreen():
    try:
        screen_more.destroy()
    except:
        pass
    try:
        screen_try.destroy()
    except:
        pass
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    global screen
    screen = customtkinter.CTk()
    
    screen.iconbitmap("icon2.ico")
    # screen.config(bg="#95949c")
    screen.geometry("850x700+50+20")
    screen.title("Spottr")
    Label(text="", bg="#242424", font=("Courier",150,"bold")).pack()
    Label(text="SPOTTR",bg ="#242424", fg="white",font=("Courier",45,"bold")).pack()
    Label(text="", bg="#242424", font=("Courier",8,"bold")).pack()
    Label(text ="Navigate with ease and locate open spots quickly. Get notified about busy lots to save time.", bg="#242424", fg="white", font=("times", 18, "italic")).pack()
    
    Label(text ="Join us in creating a greener future, one parking spot at a time. Say goodbye", bg="#242424", fg="white", font=("times", 18, "italic")).pack()
    Label(text ="to parking frustration and hello to a more sustainable and", bg="#242424", fg="white", font=("times", 18, "italic")).pack()
    #eco-friendly way of parking.
    Label(text ="eco-friendly way of parking.", bg="#242424", fg="white", font=("times", 18, "italic")).pack()
    button = customtkinter.CTkButton(text="Try it Now!",master=screen, command=try_it_now, height=50)
    button.place(x=350, y=400)
    button = customtkinter.CTkButton(text="Learn More!",master=screen, command=learn_more, height=50)
    button.place(x=350, y=470)

    #Button(text="Login",height="5",width="50",bg="green",fg="white",font=("times new roman",12,"bold")).pack()
    
    screen.mainloop()
mainscreen()
