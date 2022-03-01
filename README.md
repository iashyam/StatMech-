# StatMech-

### Hard disc simulation
In the _event driven_ approach we treat atoms as two dimmensional hard discs! We consider their collisions in pairs and also with the walls. Hence by evolving them in time with one event to another event, we can keep track of their microstates ( thier postions and momentums)! When we plot their velocity distribution, we see that they follow maxwell boltzman distribution!

### Arrow of time in the flea universe:
Two flea infested dogs are lying next to each other. The fleas hop from one dog to the other. Each flea has a name. The dynamics of the fleas is determined by a flea God who loves to play dice with this flea universe. It generates a random number, after a certain time step, between  1  and  𝑁  (where  𝑁  is the number of fleas). Depending on the number, It calls out the name of the corresponding flea, which is compelled to jump from the current dog it is inhabiting to the other. Starting with a given distribution of fleas, these ‘stochastic’ dynamics will evolve the microstate (a precise description of which flea infests which dog) and the macrostate (how many fleas on a given dog).

### Lennard Jones Fluid
We assume that the particles are interacting as lennard jones 6-12 potential. They have interaction energy that depends on their relative seperation. So we can calculate the force between them by calculating the gradient. And after that we use Newton's laws to evlove them in time. When we plot the histogram on thier speeds, we see that they follow maxwell boltzman distribution!

### Brandon Thermostate
In this case, we just do the lennard-Jones potential. But we are keeping temperature (Kinetic Energy) fixed. In every step when the Kinetic Energy changes, we scale the velocity and force the maen Kinetic Energy per particle to be fixed! hence we see the by controlling the temperature we can actually observe the phase changes in them! At the lower temperatures the crystel pattern in observed!
[](https://drive.google.com/file/d/1igC33nifqKdlBNhNm3RgYtRgJei5KHg5/view?usp=sharing)
