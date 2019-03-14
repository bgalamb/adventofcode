import re
particles = []
i = 0
with open("input.txt") as fp:
    for line in fp:
        m = re.match(r"p=<(.*)>, v=<(.*)>, a=<(.*)>", line.strip())
        p = [int(e) for e in m.group(1).strip().split(",")]
        v = [int(e) for e in m.group(2).strip().split(",")]
        a = [int(e) for e in m.group(3).strip().split(",")]
        particles.append((p,v,a,i))
        i = i+1

def step(particle):

    p = particle[0]
    v = particle[1]
    a = particle[2]

    v[0] = v[0] + a[0]
    v[1] = v[1] + a[1]
    v[2] = v[2] + a[2]

    p[0] = p[0] + v[0]
    p[1] = p[1] + v[1]
    p[2] = p[2] + v[2]

def calcdistance(particle):
    p = particle[0]
    return abs(p[0])+abs(p[1])+abs(p[2])

def calcminparticle(particles):
    minparticle = particles[0]
    for particle in particles:
        if calcdistance(particle) < calcdistance(minparticle):
            minparticle = particle

    return minparticle

i = 0
minparticletimes= 0
minparticlebefore = 0
while True:
    for particle in particles:
        step(particle)
    #print(particles)
    minparticle = calcminparticle(particles)[3]
    if minparticlebefore == minparticle:
        minparticletimes = minparticletimes + 1
    else :
        minparticlebefore = minparticle
        minparticletimes = 0

    if minparticletimes >= 10000:
        print("particle {}, times {}".format(minparticle,minparticletimes))
        break

    i = i+1
