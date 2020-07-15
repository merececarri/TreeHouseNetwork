import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import model
import math
import numpy as np
import numpy
import scipy
from scipy.spatial import Delaunay
import graphics

st.title('AECH-Treehouse')
st.subheader("Output")

# Sidebar settings
b_plot_randize = st.sidebar.button("Generate random forest and plot")

ti_angle = st.sidebar.number_input("Minimal angle")

ti_ammount = st.sidebar.number_input("Tree quantity",min_value=0, max_value=None, value=0, step=1)

area_ops = ["Surprise me", "Small", "Medium", "Big"]
sb_area = st.sidebar.selectbox("Deck area", area_ops)

b_simple_test = st.sidebar.button("Simple tests")

p_start = st.sidebar.slider("Where do you want to start?")

#definitions

def calculate_distance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  

points = np.random.rand(8, 2)
print(points) 

#starting point
initial_point = points [p_start]
xip = initial_point [0]
yip = initial_point [1]
distance_init = []

# def distance_to_init(x1, y1):
#      xip = initial_point [0]
#      yip = initial_point [1]
#      dist = math.sqrt((xip- x1)**2 + (yip - y1)**2)
#      distance_init.append(dist)  
#      return distance_init 

def pdistance_to_init(p2):
    dist = math.sqrt(((initial_point[0]-p2[0])**2)+((initial_point[1]-p2[1])**2))
    distance_init = []
    distance_init.append(dist)
    return distance_init

for p in points:
    d = pdistance_to_init(p)
    distance_init.append(d)

print(distance_init)

x_coord = []
y_coord = []

for p in points:
    xvalue = p[0]
    yvalue = p[1]
    x_coord.append(xvalue)
    y_coord.append(yvalue)

# triangle = graphics.Polygon()      
# triangle.setFill(colour)
# triangle.draw(win)

#d_ip = numpy.linalg.norm(initial_point-p)

#Button pressed

if b_plot_randize:
    points = np.random.rand(ti_ammount, 2)
    tri = Delaunay(points)

    plt.figure()
    
    #The main tree deck forest
    plt.triplot(points[:,0], points[:,1], tri.simplices)
    plt.plot(points[:,0], points[:,1], 'o')
    st.pyplot()


    clean_points = []
    clean_vertexes = []

    for triangle_points in points[tri.simplices]:
        Ax = triangle_points[0][0]
        Ay = triangle_points[0][1]

        Bx = triangle_points[1][0]
        By = triangle_points[1][1]

        Cx = triangle_points[2][0]
        Cy = triangle_points[2][1]

        a = calculate_distance(Bx, By, Cx, Cy)
        b = calculate_distance(Cx, Cy, Ax, Ay)
        c = calculate_distance(Ax, Ay, Bx, By)

        #Get the angles
        Trigonometria
        cos_A_angle = ( ((b**2) + (c**2) - (a**2)) / (2*b*c) )
        cos_B_angle = ( ((c**2) + (a**2) - (b**2)) / (2*c*a) )
        cos_C_angle = ( ((a**2) + (b**2) - (c**2)) / (2*a*b) )

        A_angle = math.degrees(math.acos(cos_A_angle))
        B_angle = math.degrees(math.acos(cos_B_angle))
        C_angle = math.degrees(math.acos(cos_C_angle))

        if A_angle <= ti_angle or B_angle <= ti_angle or C_angle <= ti_angle:
            continue
        else:

            clean_vertexes.append([(Ax, Ay), (Bx, By)])
            clean_vertexes.append([(Bx, By), (Cx, Cy)])
            clean_vertexes.append([(Cx, Cy), (Ax, Ay)])

    #The cleaned decks
    lc = mc.LineCollection(clean_vertexes, linewidths=2)
    fig, ax = plt.subplots()
    ax.add_collection(lc)

    plt.plot(points[:,0], points[:,1], 'o')

    st.pyplot()

    
if b_simple_test:
    xy = np.asarray([
        [-0.101, 0.872], [-0.080, 0.883]])
    x = np.degrees(xy[:, 0])
    y = np.degrees(xy[:, 1])

    triangles = np.asarray([
        [67, 66,  1], [65,  2, 66], [33, 72, 38],
        [33, 38, 34], [37, 35, 38], [34, 38, 35], [35, 37, 36]])

    print(len(xy))
    print(len(triangles))

    fig2, ax2 = plt.subplots()
    ax2.set_aspect('equal')
    ax2.triplot(x, y, triangles, 'go-', lw=1.0)
    ax2.set_title('triplot of user-specified triangulation')
    ax2.set_xlabel('Longitude (degrees)')
    ax2.set_ylabel('Latitude (degrees)')
    st.pyplot()