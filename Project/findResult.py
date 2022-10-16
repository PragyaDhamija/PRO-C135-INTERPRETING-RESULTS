import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("Project/StarsFiltered.csv")

name = df["StarName"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
grav = df["Gravity"].to_list()

#plt.figure(figsize=(10,5))
plt.title("Name VS Mass")
plt.xlabel('Name of Stars')
plt.ylabel('Mass of Stars')
plt.bar(name, mass)

plt.figure(figsize=(30,5))
plt.title("Name VS Radius")
plt.xlabel('Name of Stars')
plt.ylabel('Radius of Stars')
plt.bar(name,radius)

plt.figure(figsize=(10,5))
plt.title("Name VS Gravity")
plt.xlabel('Name of Stars')
plt.ylabel('Gravity of Stars')
plt.bar(name,grav)

plt.figure(figsize=(10,5))
plt.title("Name VS Distance")
plt.xlabel('Name of Stars')
plt.ylabel('Distance of Stars')
plt.bar(name,dist)

plt.show()

