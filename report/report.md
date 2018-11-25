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
Symbolic Dynamics is a technique of studying dynamics of a system. Here we chop up the dynamical trajectories of a system into discrete pieces and attach to each piece, a symbol. Now based on the sequences of the symbol created by the trajetory we describe the dynamics of the system. 

Herein arises the motivation for this project: **Use symbolic dynamics on Chaotic Attractors**. Here, we have used pithces from a musical piece as our symbols. But note that any context dependent sequence of data can be used.  Further we have used the Lorenz attractor, though any other 'Strange Attractor' can also be used. 

#Implementation details
