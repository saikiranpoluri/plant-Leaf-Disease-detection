import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import shutil  # This module helps in automating process of copying,moving and removal of files and directories
import \
    os  # dealing with directories...The OS module in Python provides a way of using operating system dependent functionality. The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux
import \
    sys  # The sys module provides information about constants, functions and methods of the Python interpreter. dir(system) gives a summary of the available constants, functions and methods. Another possibility is the help() function. Using help(sys) provides valuable detail information.
from PIL import Image, \
    ImageTk  # Python Imaging Library. Python Imaging Library (abbreviated as PIL) (in newer versions known as Pillow) is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats. It is available for Windows, Mac OS X and Linux.
from pip._vendor.cachecontrol import controller

window = tk.Tk()
window.title("Dr. Plant")
window.geometry("500x600")
window.configure(background="lightpink")
title = tk.Label(text="   Click below to choose picture for testing disease", background="lightpink", fg="green",
                 font=("times new roman", 17))
title.grid()


def targetspot():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("500x600")
    window1.configure(background="lightpink")

    def exit():
        window1.destroy()

    rem = "The remedies for target spot  are:\n\n "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)
    rem1 = "Spray with protectant fungicides after first symptoms appear.\n Consult with your local extension agent for \n" \
           "fungicides available in your region. Remove affected\n debris to prevent carryover into the next crop.\n Use " \
           "an adequate period of crop rotation.\n Genetic resistance to this fungus has been documented in \n tomato and " \
           "soybean but commercial varieties are\n not yet available. "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)
    window1.mainloop()


def mtargetspot():
    window.destroy()
    window2 = tk.Tk()

    window2.title("Dr. Plant")

    window2.geometry("500x510")
    window2.configure(background="lightpink")

    def exit():
        window2.destroy()

    def targetspot():
        window2.destroy()
        window1 = tk.Tk()
        window1.title("Dr. Plant")
        window1.geometry("500x510")
        window1.configure(background="lightpink")

        def exit():
            window1.destroy()

        rem = "The remedies for target spot  are:\n\n "
        remedies = tk.Label(text=rem, background="lightpink",
                            fg="Brown", font=("", 15))
        remedies.grid(column=0, row=7, padx=10, pady=10)
        rem1 = "Spray with protectant fungicides after first symptoms appear.\n Consult with your local extension agent for \n" \
               "fungicides available in your region. Remove affected\n debris to prevent carryover into the next crop.\n Use " \
               "an adequate period of crop rotation.\n Genetic resistance to this fungus has been documented in \n tomato and " \
               "soybean but commercial varieties are\n not yet available. "
        remedies1 = tk.Label(text=rem1, background="lightpink",
                             fg="Black", font=("", 12))
        remedies1.grid(column=0, row=8, padx=10, pady=10)

        button = tk.Button(text="Exit", command=exit)
        button.grid(column=0, row=9, padx=20, pady=20)
        button2 = tk.Button(text="back", command=mainwin)
        button2.grid(column=0, row=10, padx=10, pady=10)
        window1.mainloop()

    rem = "The target spot  is caused due to :\n\n "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)
    rem1 = "Disease development is favored by warm temperatures and \n extended periods of leaf wetness. The optimal " \
           "temperature range for disease \n development is 20–28 °C with 16 hr or more of leaf wetness.\n The fungus " \
           "sporulates abundantly on rain-moistened crop debris or\n from target spot lesions on dead tomato leaves. \n" \
           "The fungus can colonize weeds or other crop plants.\n It remains viable for up to two years. "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)
    button = tk.Button(text="remedies", command=targetspot)
    button.grid(column=0, row=9, padx=20, pady=20)

    window2.mainloop()


def yellowcurlvirus():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("500x600")
    window1.configure(background="lightpink")

    def exit():
        window1.destroy()

    rem = "The remedies for Yellow leaf curl virus are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)
    rem1 = " Monitor the field, handpick diseased plants and bury them. \n  Use sticky yellow plastic traps. \n  Spray insecticides such as organophosphates, carbametes \nduring the seedliing stage.  Use copper fungicites\n"
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def myellowcurlvirus():
    window.destroy()
    window2 = tk.Tk()

    window2.title("Dr. Plant")

    window2.geometry("500x600")
    window2.configure(background="lightpink")

    def exit():
        window2.destroy()

    def yellowcurlvirus():
        window2.destroy()
        window1 = tk.Tk()

        window1.title("Dr. Plant")

        window1.geometry("500x510")
        window1.configure(background="lightpink")

        def exit():
            window1.destroy()

        rem = "The remedies for Yellow leaf curl virus are: "
        remedies = tk.Label(text=rem, background="lightpink",
                            fg="Brown", font=("", 15))
        remedies.grid(column=0, row=7, padx=10, pady=10)
        rem1 = "  Monitor the field, handpick diseased plants and bury them. \n  Use sticky yellow plastic traps. \n  Spray insecticides such as organophosphates, carbametes \nduring the seedliing stage.  Use copper fungicites\n"
        remedies1 = tk.Label(text=rem1, background="lightpink",
                             fg="Black", font=("", 12))
        remedies1.grid(column=0, row=8, padx=10, pady=10)

        button = tk.Button(text="Exit", command=exit)
        button.grid(column=0, row=9, padx=20, pady=20)

        window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.

    rem = "The  Yellow leaf curl virus is: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)
    rem1 = " This disease is transmitted by whitefly (Bemisia tabaci).\n Leaf curl disease is characterized by severe stunting of the \n plants with downward rolling and crinkling of the leaves.\nThe infected plants look pale and produce more lateral branches \n giving a bushy appearance. The infected plants remain stunted"
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="remedies", command=yellowcurlvirus)
    button.grid(column=0, row=9, padx=20, pady=20)

    window2.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def bacterialspot():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("500x600")
    window1.configure(background="lightpink")

    def exit():
        window1.destroy()

    rem = "The remedies for bacterial spot are are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Bacterial spot is difficult to control once it appears\n inthe field. Disease-free seed and seedlings \n" \
           "should always be used and the crop should be rotated\n with non-host crops so as to avoid last years crop \n" \
           "residue. Seed treatment with mercuric chloride (1:1000)\n is also recommended for control of disease.\n " \
           "Spraying with a combination of copper and organic \nfungicides in a regular preventative spray program at \n5 " \
           "to 10 day intervals or Spraying with Agrimycin-100\n (100 ppm) thrice at 10 days intervals effectively\n " \
           "controls the disease. "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def mbacterialspot():
    window.destroy()
    window2 = tk.Tk()

    window2.title("Dr. Plant")

    window2.geometry("500x600")
    window2.configure(background="lightpink")

    def exit():
        window2.destroy()

    def bacterialspot():
        window2.destroy()
        window1 = tk.Tk()

        window1.title("Dr. Plant")

        window1.geometry("500x600")
        window1.configure(background="lightpink")

        def exit():
            window1.destroy()

        rem = "The remedies for bacterial spot are are: "
        remedies = tk.Label(text=rem, background="lightpink",
                            fg="Brown", font=("", 15))
        remedies.grid(column=0, row=7, padx=10, pady=10)

        rem1 = "Bacterial spot is difficult to control once it appears\n inthe field. Disease-free seed and seedlings \n" \
               "should always be used and the crop should be rotated\n with non-host crops so as to avoid last years crop \n" \
               "residue. Seed treatment with mercuric chloride (1:1000)\n is also recommended for control of disease.\n " \
               "Spraying with a combination of copper and organic \nfungicides in a regular preventative spray program at \n5 " \
               "to 10 day intervals or Spraying with Agrimycin-100\n (100 ppm) thrice at 10 days intervals effectively\n " \
               "controls the disease. "
        remedies1 = tk.Label(text=rem1, background="lightpink",
                             fg="Black", font=("", 12))
        remedies1.grid(column=0, row=8, padx=10, pady=10)

        button = tk.Button(text="Exit", command=exit)
        button.grid(column=0, row=9, padx=20, pady=20)

        window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.

    rem = "The  bacterial spot is: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Moist weather and splattering rains are conducive \nto disease development.Most outbreaks of the disease can \nbe traced back to heavy rainstorms that occur in the area. \nInfected leaves show small,brown, water soaked, \ncircular spots surrounded with yellowish halo"
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Remedies", command=bacterialspot)
    button.grid(column=0, row=9, padx=20, pady=20)

    window2.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def earlyblight():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("500x600")
    window1.configure(background="lightpink")

    def exit():
        window1.destroy()

    rem = "The remedies for early blight  are are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Removal and destruction of the affected plant parts. \n Practicing crop rotation helps to minimize the\n " \
           "disease incidence. Spraying the crop with Difolatan (0.2%),\n Dithane M-45 (0.2%) or Bavistin (0.1%) is \n" \
           "recommended for effective disease control. "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def mearlyblight():
    window.destroy()
    window2 = tk.Tk()

    window2.title("Dr. Plant")

    window2.geometry("500x600")
    window2.configure(background="lightpink")

    def exit():
        window2.destroy()

    def earlyblight():
        window2.destroy()
        window1 = tk.Tk()

        window1.title("Dr. Plant")

        window1.geometry("500x600")
        window1.configure(background="lightpink")

        def exit():
            window1.destroy()

        rem = "The early blight  is: "
        remedies = tk.Label(text=rem, background="lightpink",
                            fg="Brown", font=("", 15))
        remedies.grid(column=0, row=7, padx=10, pady=10)

        rem1 = "The appearance of circular or irregular dark spots\n on the lower, more mature leaves is one of the\n " \
               "first symptoms of infection. Eventually, the spots \nenlarge into a series of concentric rings \n" \
               "surrounded by a yellow area. The entire leaf may \nbe killed and will drop off the plant. Early blight \n" \
               "can result in extensive defoliation, exposing fruit\n to sunscald and reducing yields. This disease \n" \
               "typically progresses from the base of the plant, upward. "

        remedies1 = tk.Label(text=rem1, background="lightpink",
                             fg="Black", font=("", 12))
        remedies1.grid(column=0, row=8, padx=10, pady=10)

        button = tk.Button(text="Exit", command=exit)
        button.grid(column=0, row=9, padx=20, pady=20)

        window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.

    rem = "The remedies for early blight  are are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Removal and destruction of the affected plant parts. \n Practicing crop rotation helps to minimize the\n " \
           "disease incidence. Spraying the crop with Difolatan (0.2%),\n Dithane M-45 (0.2%) or Bavistin (0.1%) is \n" \
           "recommended for effective disease control. "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Remedies", command=earlyblight)
    button.grid(column=0, row=9, padx=20, pady=20)

    window2.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def latebl():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("500x600")
    window1.configure(background="lightpink")

    def exit():
        window1.destroy()

    rem = "The remedies for Late Blight are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Monitor the field, remove and destroy infected leaves. \n  Treat organically with copper spray. \n  Use " \
           "chemical fungicides,the best of which for tomatoes is chlorothalonil. "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def mlatebl():
    window.destroy()
    window2 = tk.Tk()

    window2.title("Dr. Plant")

    window2.geometry("500x600")
    window2.configure(background="lightpink")

    def exit():
        window2.destroy()

    def latebl():
        window2.destroy()
        window1 = tk.Tk()

        window1.title("Dr. Plant")

        window1.geometry("500x600")
        window1.configure(background="lightpink")

        def exit():
            window1.destroy()

        rem = "The remedies for Late Blight are: "
        remedies = tk.Label(text=rem, background="lightpink",
                            fg="Brown", font=("", 15))
        remedies.grid(column=0, row=7, padx=10, pady=10)

        rem1 = "Monitor the field, remove and destroy infected leaves. \n  Treat organically with copper spray. \n  Use " \
               "chemical fungicides,the best of which for tomatoes is chlorothalonil. "
        remedies1 = tk.Label(text=rem1, background="lightpink",
                             fg="Black", font=("", 12))
        remedies1.grid(column=0, row=8, padx=10, pady=10)

        button = tk.Button(text="Exit", command=exit)
        button.grid(column=0, row=9, padx=20, pady=20)

        window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.

    rem = "The Late Blight is: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Late blight occurs when humid conditions coincide with\n mild temperatures for prolonged periods.Lesions produced \non the leaves are at first irregular, rather large, greenish-black \nand water-soaked. These areas enlarge rapidly, becoming brown\n, and under humid conditions, develop a white moldy growth \n near the margins of the diseased area on the lower surface of \n the leaves or on stems "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Remedies", command=latebl)
    button.grid(column=0, row=9, padx=20, pady=20)

    window2.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def septorialleafspot():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("500x600")
    window1.configure(background="lightpink")

    def exit():
        window1.destroy()

    rem = "The remedies for septrial leaf spot are are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Removal and destruction of the affected plant parts. Seed treatment\n with Thiram or Dithane M-45 (2 g/kg  " \
           "seed) is useful in \nchecking seed borne infection.  In the field spraying with \nDithane Z-78 (0.2%)  " \
           "effectively controls the disease. "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def mseptorialleafspot():
    window.destroy()
    window2 = tk.Tk()

    window2.title("Dr. Plant")

    window2.geometry("500x600")
    window2.configure(background="lightpink")

    def exit():
        window2.destroy()

    def septorialleafspot():
        window2.destroy()
        window1 = tk.Tk()

        window1.title("Dr. Plant")

        window1.geometry("500x600")
        window1.configure(background="lightpink")

        def exit():
            window1.destroy()

        rem = "The remedies for septrial leaf spot are are: "
        remedies = tk.Label(text=rem, background="lightpink",
                            fg="Brown", font=("", 15))
        remedies.grid(column=0, row=7, padx=10, pady=10)

        rem1 = "Removal and destruction of the affected plant parts. Seed treatment\n with Thiram or Dithane M-45 (2 g/kg  " \
           "seed) is useful in \nchecking seed borne infection.  In the field spraying with \nDithane Z-78 (0.2%)  " \
           "effectively controls the disease. "
        remedies1 = tk.Label(text=rem1, background="lightpink",
                             fg="Black", font=("", 12))
        remedies1.grid(column=0, row=8, padx=10, pady=10)

        button = tk.Button(text="Exit", command=exit)
        button.grid(column=0, row=9, padx=20, pady=20)

        window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.

    rem = "The septrial leaf spot is: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Septoria leaf spot usually appears on the lower leaves \nafter the first fruit sets. Spots are circular, about \n1/16 to 1/4 inch in diameter with dark brown margins and tan\n to gray centers with small black fruiting structures.\n Characteristically, there are many spots per leaf. \nThis disease spreads upwards from oldest to youngest \ngrowth. If leaf lesions are numerous, the leaves turn \nslightly yellow, then brown, and then wither. \nFruit infection is rare."
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="remedies", command=septorialleafspot)
    button.grid(column=0, row=9, padx=20, pady=20)

    window2.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def spidermite():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("500x600")
    window1.configure(background="lightpink")

    def exit():
        window1.destroy()

    rem = "The remedies for spidermite are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "I've used to control a mild infestation of spider mites: \nMix 1/4 cup apple cider vinegar (white vinegar \n" \
           "is fine too) with 1 cup of water, 1 t of baking \nsoda & a few drops of mild dish soap into a spray bottle "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def mspidermite():
    window.destroy()
    window2 = tk.Tk()

    window2.title("Dr. Plant")

    window2.geometry("500x600")
    window2.configure(background="lightpink")

    def exit():
        window2.destroy()

    def spidermite():
        window2.destroy()
        window1 = tk.Tk()

        window1.title("Dr. Plant")

        window1.geometry("500x600")
        window1.configure(background="lightpink")

        def exit():
            window1.destroy()

        rem = "The remedies for spidermite are: "
        remedies = tk.Label(text=rem, background="lightpink",
                            fg="Brown", font=("", 15))
        remedies.grid(column=0, row=7, padx=10, pady=10)

        rem1 = "I've used to control a mild infestation of spider mites: \nMix 1/4 cup apple cider vinegar (white vinegar \n" \
               "is fine too) with 1 cup of water, 1 t of baking \nsoda & a few drops of mild dish soap into a spray bottle "
        remedies1 = tk.Label(text=rem1, background="lightpink",
                             fg="Black", font=("", 12))
        remedies1.grid(column=0, row=8, padx=10, pady=10)

        button = tk.Button(text="Exit", command=exit)
        button.grid(column=0, row=9, padx=20, pady=20)

        window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.

    rem = "The spidermite is: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = " Large infestations cause visible damage. Leaves first show\n patterns of tiny spots or stipplings. They may change color, \ncurl and fall off. The mites activity is visible in the tight\n webs that are formed under leaves and along stem"
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="remedies", command=spidermite)
    button.grid(column=0, row=9, padx=20, pady=20)

    window2.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def mosaicvirus():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("500x600")
    window1.configure(background="lightpink")

    def exit():
        window1.destroy()

    rem = "The remedies for mosaic virus are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Seeds from disease free healthy plants should be\n selected for sowing. Soaking of the seeds in a solution\n " \
           "of Trisodium Phosphate (90 g/litre of water) a day\n before sowing helps to reduce thedisease incidence. \n" \
           "The seeds should be thoroughly rinsed and dried in \n shade. In the nursery all the infected plants should \n" \
           "be removed carefully and destroyed. Seedlings with\n infected with the viral disease should not be used for \n" \
           "transplanting. Crop rotation with crops other than\n tobacco, potato, chilli, capsicum, brinjal,\n " \
           "etc. should be undertaken. "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def mmosaicvirus():
    window.destroy()
    window2 = tk.Tk()

    window2.title("Dr. Plant")

    window2.geometry("500x600")
    window2.configure(background="lightpink")

    def exit():
        window2.destroy()

    def mosaicvirus():
        window2.destroy()
        window1 = tk.Tk()

        window1.title("Dr. Plant")

        window1.geometry("500x600")
        window1.configure(background="lightpink")

        def exit():
            window1.destroy()

        rem = "The remedies for mosaic virus are: "
        remedies = tk.Label(text=rem, background="lightpink",
                            fg="Brown", font=("", 15))
        remedies.grid(column=0, row=7, padx=10, pady=10)

        rem1 = "Seeds from disease free healthy plants should be\n selected for sowing. Soaking of the seeds in a solution\n " \
               "of Trisodium Phosphate (90 g/litre of water) a day\n before sowing helps to reduce thedisease incidence. \n" \
               "The seeds should be thoroughly rinsed and dried in \n shade. In the nursery all the infected plants should \n" \
               "be removed carefully and destroyed. Seedlings with\n infected with the viral disease should not be used for \n" \
               "transplanting. Crop rotation with crops other than\n tobacco, potato, chilli, capsicum, brinjal,\n " \
               "etc. should be undertaken. "
        remedies1 = tk.Label(text=rem1, background="lightpink",
                             fg="Black", font=("", 12))
        remedies1.grid(column=0, row=8, padx=10, pady=10)

        button = tk.Button(text="Exit", command=exit)
        button.grid(column=0, row=9, padx=20, pady=20)

        window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.

    rem = "The mosaic virus is: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "They are often seen as a general mottling or mosaic appearance\n on foliage. When the plant is severely " \
           "affected,\n leaves may look akin to ferns with raised dark green regions. \nLeaves may also become " \
           "stunted. "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="remedies", command=mosaicvirus)
    button.grid(column=0, row=9, padx=20, pady=20)

    window2.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def leafmold():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("500x600")
    window1.configure(background="lightpink")

    def exit():
        window1.destroy()

    rem = "The remedies for Leaf mold are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Remove and destroy all affected plant parts. For plants growing \nunder cover, increase ventilation and, " \
           "if possible, the \n space between plants. Try to avoid wetting the leaves when \n watering plants, especially " \
           "when watering in the evening,\n Copper-based fungicides can be used to control diseases on tomatoes "
    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def mleafmold():
    window.destroy()
    window2 = tk.Tk()

    window2.title("Dr. Plant")

    window2.geometry("500x600")
    window2.configure(background="lightpink")

    def exit():
        window2.destroy()

    def leafmold():
        window2.destroy()
        window1 = tk.Tk()

        window1.title("Dr. Plant")

        window1.geometry("500x600")
        window1.configure(background="lightpink")

        def exit():
            window1.destroy()

        rem = "The remedies for Leaf mold are: "
        remedies = tk.Label(text=rem, background="lightpink",
                            fg="Brown", font=("", 15))
        remedies.grid(column=0, row=7, padx=10, pady=10)

        rem1 = "Remove and destroy all affected plant parts. For plants growing \nunder cover, increase ventilation and, " \
               "if possible, the \n space between plants. Try to avoid wetting the leaves when \n watering plants, especially " \
               "when watering in the evening,\nCopper-based fungicides can be used to control diseases on tomatoes"
        remedies1 = tk.Label(text=rem1, background="lightpink",
                             fg="Black", font=("", 12))
        remedies1.grid(column=0, row=8, padx=10, pady=10)

        button = tk.Button(text="Exit", command=exit)
        button.grid(column=0, row=9, padx=20, pady=20)

        window1.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.

    rem = "The remedies for Leaf mold are: "
    remedies = tk.Label(text=rem, background="lightpink",
                        fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = "Tomato leaf mould symptoms include extensive discolouration\n with leaves or fruit turning brown, and bleached white\n spots on flower petals "

    remedies1 = tk.Label(text=rem1, background="lightpink",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Remedies", command=leafmold)
    button.grid(column=0, row=9, padx=20, pady=20)

    window2.mainloop()  # mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run.


def analysis():
    import cv2  # working with, mainly resizing, images (open source computer vision)
    import \
        numpy as np  # dealing with arrays operations...since images are stored in a matrix form we should numpy to process the images
    import os  # dealing with directories
    from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
    from tqdm import tqdm  # a nice pretty percentage bar for tasks.
    verify_dir = 'testpicture'
    IMG_SIZE = 50
    LR = 1e-3
    MODEL_NAME = 'healthyvsunhealthy3-{}-{}.model'.format(LR, '2conv-basic')

    # https://medium.com/@curiousily/tensorflow-for-hackers-part-iii-convolutional-neural-networks-c077618e590b
    def process_verify_data():
        verifying_data = []
        for img in tqdm(os.listdir(verify_dir)):
            path = os.path.join(verify_dir, img)
            img_num = img.split('.')[0]
            img = cv2.imread(path, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            verifying_data.append([np.array(img), img_num])
        np.save('verify_data.npy', verifying_data)
        return verifying_data

    verify_data = process_verify_data()
    # verify_data = np.load('verify_data.npy')

    import tflearn
    from tflearn.layers.conv import conv_2d, max_pool_2d
    from tflearn.layers.core import input_data, dropout, fully_connected
    from tflearn.layers.estimator import regression
    import tensorflow as tf
    tf.reset_default_graph()

    convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 3], name='input')

    convnet = conv_2d(convnet, 32, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 64, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 128, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 32, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 64, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = fully_connected(convnet, 1024, activation='relu')
    convnet = dropout(convnet, 0.8)

    convnet = fully_connected(convnet, 10, activation='softmax')
    convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(convnet, tensorboard_dir='log')

    if os.path.exists('{}.meta'.format(MODEL_NAME)):
        model.load(MODEL_NAME)
        print('model loaded!')

    import matplotlib.pyplot as plt

    fig = plt.figure()

    for num, data in enumerate(verify_data):

        img_num = data[1]
        img_data = data[0]

        y = fig.add_subplot(3, 4, num + 1)
        orig = img_data
        data = img_data.reshape(IMG_SIZE, IMG_SIZE, 3)
        # model_out = model.predict([data])[0]
        model_out = model.predict([data])[0]

        if np.argmax(model_out) == 0:
            str_label = 'Tomato__Target_Spot'
        elif np.argmax(model_out) == 1:
            str_label = 'Tomato__Tomato_YellowLeaf__Curl_Virus'
        elif np.argmax(model_out) == 2:
            str_label = 'Tomato_Bacterial_spot'
        elif np.argmax(model_out) == 3:
            str_label = 'Tomato_Early_blight'
        elif np.argmax(model_out) == 4:
            str_label = 'Tomato_healthy'
        elif np.argmax(model_out) == 5:
            str_label = 'Tomato_Late_blight'
        elif np.argmax(model_out) == 6:
            str_label = 'Tomato_Septoria_leaf_spot'
        elif np.argmax(model_out) == 7:
            str_label = 'Tomato_Spider_mites_Two_spotted_spider_mite'
        elif np.argmax(model_out) == 8:
            str_label = 'Tomato__Tomato_mosaic_virus'
        elif np.argmax(model_out) == 9:
            str_label = 'Tomato_Leaf_Mold'

        if str_label == 'Tomato_healthy':
            status = "HEALTHY"
        else:
            status = "UNHEALTHY"

        message = tk.Label(text='Status: ' + status, background="lightpink",
                           fg="Brown", font=("", 15))
        message.grid(column=0, row=3, padx=10, pady=10)
        if str_label == 'Tomato__Target_Spot':
            diseasename = "Tomato Target Spot"
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)
            button31 = tk.Button(text="more info", command=mtargetspot)
            button31.grid(column=0, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightpink", fg="Brown", font=("", 15))
            r.grid(column=0, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=targetspot)
            button3.grid(column=0, row=7, padx=10, pady=10)

        elif str_label == 'Tomato__Tomato_YellowLeaf__Curl_Virus':
            diseasename = "Tomato Tomato YellowLeaf Curl Virus "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)
            button31 = tk.Button(text="more info", command=myellowcurlvirus)
            button31.grid(column=0, row=5, padx=10, pady=10)

            r = tk.Label(text='Click below for remedies...', background="lightpink", fg="Brown", font=("", 15))
            r.grid(column=0, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=yellowcurlvirus)
            button3.grid(column=0, row=7, padx=10, pady=10)

        elif str_label == 'Tomato_Bacterial_spot':
            diseasename = "Tomato Bacterial spot "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)
            button31 = tk.Button(text="more info", command=mbacterialspot)
            button31.grid(column=0, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightpink", fg="Brown", font=("", 15))
            r.grid(column=0, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=bacterialspot)
            button3.grid(column=0, row=7, padx=10, pady=10)

        elif str_label == 'Tomato_Early_blight':
            diseasename = "Tomato Early blight "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)
            button31 = tk.Button(text="more info", command=mearlyblight)
            button31.grid(column=0, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightpink", fg="Brown", font=("", 15))
            r.grid(column=0, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=earlyblight)
            button3.grid(column=0, row=7, padx=10, pady=10)
        elif str_label == 'Tomato_healthy':
            diseasename = "Tomato healthy "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)

        elif str_label == 'Tomato_Late_blight':
            diseasename = "Tomato Late blight "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)
            button31 = tk.Button(text="more info", command=mlatebl)
            button31.grid(column=0, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightpink", fg="Brown", font=("", 15))
            r.grid(column=0, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=latebl)
            button3.grid(column=0, row=7, padx=10, pady=10)
        elif str_label == 'Tomato_Septoria_leaf_spot':
            diseasename = "Tomato Septoria leaf spot "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)
            button31 = tk.Button(text="more info", command=mseptorialleafspot)
            button31.grid(column=0, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightpink", fg="Brown", font=("", 15))
            r.grid(column=0, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=septorialleafspot)
            button3.grid(column=0, row=7, padx=10, pady=10)
        elif str_label == 'Tomato_Spider_mites_Two_spotted_spider_mite':
            diseasename = "Tomato Spider mites Two spotted spider mite "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)
            button31 = tk.Button(text="more info", command=mspidermite)
            button31.grid(column=0, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightpink", fg="Brown", font=("", 15))
            r.grid(column=0, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=spidermite)
            button3.grid(column=0, row=7, padx=10, pady=10)
        elif str_label == 'Tomato__Tomato_mosaic_virus':
            diseasename = "Tomato Tomato mosaic virus "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)
            button31 = tk.Button(text="more info", command=mmosaicvirus)
            button31.grid(column=0, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightpink", fg="Brown", font=("", 15))
            r.grid(column=0, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=mosaicvirus)
            button3.grid(column=0, row=7, padx=10, pady=10)
        elif str_label == 'Tomato_Leaf_Mold':
            diseasename = "Tomato Leaf Mold "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightpink",
                               fg="Black", font=("", 15))
            disease.grid(column=0, row=4, padx=10, pady=10)
            button31 = tk.Button(text="more info", command=mleafmold)
            button31.grid(column=0, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightpink", fg="Brown", font=("", 15))
            r.grid(column=0, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=leafmold)
            button3.grid(column=0, row=7, padx=10, pady=10)


def openphoto():
    dirPath = "testpicture"
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath + "/" + fileName)

    # C:/Users/sai kiran/Downloads is the location of the image which you want to test..... you can change it according to the image location you have
    # While working with GUI one may need to open files and read data from it or may require to write data in that particular file
    # With the help of GUI, you may not require to specify the path of any file but you can directly open a file and read it’s content.
    fileName = askopenfilename(initialdir='C:/Users/saiki/Downloads', title='Select image for analysis ',
                               filetypes=[('image files', '.JPG')])
    dst = "C:/Users/saiki/Desktop/plantleafdiseasedetection/testpicture"
    shutil.copy(fileName, dst)
    load = Image.open(fileName)
    render = ImageTk.PhotoImage(
        load)  # The PhotoImage class is used to display images (either grayscale or true color images) in labels, buttons, canvases, and text widgets.
    # You can use the PhotoImage class whenever you need to display an icon or an image in a Tkinter application.
    img = tk.Label(image=render, height="250", width="500")  # to show the image selected
    img.image = render
    img.place(x=0, y=0)
    img.grid(column=0, row=1, padx=10, pady=10)
    title.destroy()
    # button.destroy()
    button2 = tk.Button(text="Analyse Image", command=analysis)
    button2.grid(column=0, row=2, padx=10, pady=10)


def mainwin():
    buttonx = tk.Button(text="Get Photo", command=openphoto)
    buttonx.grid(column=0, row=1, padx=10, pady=10)


mainwin()
window.mainloop()

