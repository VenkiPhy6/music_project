#Motivation
##Chaotic Attractors
Chaotic dynamics is a type of dynamics which is characterised by a sensitive dependance on initial conditions. That is, a small change in the initial conditions results in a very different trajectory in the state space. The trajectory of systems that follow such dynamics, in the state space, usually end up at a fixed point or a limit cycle. But some systems end up in 'Strange Attractors'. One such system is the Lorenz system of convection currents. The 'Strange Attractor' that this system eventually ends up in is called the 'Lorenz Attractor'.  It follows dynamics as dictated by the below set of 1st order differential equations:

$$\begin{align}
\dot x &= \sigma (y - x) \\
\dot y &= rx - y - xz \\
\dot z &= xy - bz 
\end{align}
$$ 

##Symbolic dynamics
Symbolic Dynamics is a technique of studying dynamics of a system. Here we chop up the dynamical trajectories of a system into discrete pieces and attach to each piece, a symbol. Now based on the sequences of the symbols created by the different trajetories we describe the dynamics of the system. 

Herein arises the motivation for this project: **Use symbolic dynamics on Chaotic Attractors**. Here, we have used pithces from a musical piece as our symbols. But note that any context dependent sequence of data can be used.  Further we have used the Lorenz attractor, though any other 'Strange Attractor' can also be used. We use the chaotic attractor to create musical variations on a given given musical piece. 

#Implementation details
##Obtaining the Lorenz attractor
To obtain the Lorenz attractor, we solve the aforementioned set of equations using the 4th order Runge Kutta solver. We use a step size of 0.01 for 5000 steps. We used the parameter values: r = 28, $\sigma$ = 10 and b = 8/3 and give the requisite initial condition. The attractor obtained with initial condition $x = 1.0$, $y=1.0$, $z=1.0$ is shown below:

![Figure 1](/files/lorenz.png)


##The symbols
Now that we have the attractor, we need the symbols. As mentioned before, we use the pitch sequence of a musical piece. In this project, we used J. S. Bach’s Prelude in C Major from The Well-Tempered Clavier, Book I as a musical piece.  Its sheet music is available in the public domain. It contains 34 measures/bars and two parts. One part is in the Treble Clef and the other is in the Bass Clef. We use the Treble Cleff part alone to make the analysis simpler. This part is shown below. It has only 33 measures since we have also ignored the final chord for simplicity, again. The sheet music was downloaded as a MuseScore xml file. MuseScore is a free music composition and notation software. Further manipulations of this xml file was carried out with music21, a Python library for computational musicology. 

![Figure 2](/files/original.png)

##Creating the variation
Now, we create the reference trajectory. This is the trajectory to which the original piece(in Figure 2) is mapped to. It is generated with initial condition $x = 1.0$, $y=1.0$, $z=1.0$. Then we create a new trajectory with initial condition $x = 0.999$, $y=1.0$, $z=1.0$ with all the other parameters kept the same as before. To this new trajectory we map the pitches based on a rule. Call the points of the reference trajectory $x_i$ where $i$ refers to the $i^{th}$ point in the trajectory. Then, call the points of the new trajectory $x_j'$ where $j$ refers to the $j^{th}$ point in the trajectory. Now let pitch $p_i$ be associated with the $i^{th}$ point of the reference trajectory. Then the rule for mapping pitches to the new trajectories is:
$$f(x_j') = p_{g(j)}$$ 
where $g(j)$ represents the index of the smallest $x_i$ for which $x_i \ge x_j'$. Note that in music21, shuffling a (Python) list of pitches(notes) doesn't change the sequence of pitches in the stream object. Instead one has to change the offset of the pitches i.e the position of the notes from the beginning of the stream object, to change the sequence. Thus, in the Python script, instead of applying the above rule to pitches directly, we apply it to the offsets of the pitches. Nevertheless, the result is the same and it is as shown below. 

![Figure 3](/files/variation1.png) 

#Results
