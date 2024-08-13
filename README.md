# Conway Game of Life Experiments

## A spiraling collection of virtual measurements

_authored by:_

p4tt3rn p0pp3r5 . y0ch0 mute8r

<img width="267" alt="Screen Shot 2023-06-29 at 12 16 57 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/38a04458-1c28-481f-93eb-ec9ea1a0a092">

```
1 0 1
1 0 1
1 1 1
```

Scripts:
<br/>
[https://github.com/tboie/universal_phreak_generator/blob/main/public/scripts](https://github.com/tboie/universal_phreak_generator/blob/main/public/scripts)

<br/>

- Does geometric sequence emerge from a grid of cells?
- How to apply geometric sequence?
- What if grid diagrams visually match sequence reaction?

<br/>

## System mechanics visualization

Cell:
<br/>
<img width="480" alt="locality diagram 0 layer point grid lines" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/658a7a80-1350-4c2c-b2e6-a77620efcd60"/>
<br/>
<br/>

Next Layer Locality Diagram of Cell:
<br/>
<img width="480" alt="locality diagram 1 layer grid lines" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/74e53f46-fea5-4b9e-b044-aec10a3ae2a5">
<br/>
<br/>

Next Layer Locality Diagram of Cell:
<br/>
<img width="480" alt="locality diagram 2 layer grid lines" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/06240771-b898-4c0e-87e4-f5b5a7d1b6b5">
<br/>
<br/>

Combining Layers:
<br/>
<img width="480" alt="locality diagram combined layers grid lines" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/c612b15c-dec0-42ab-9b6f-235ae5e617f4">
<br/>
<br/>

8 Layer Locality Diagram of Cell (no grid lines)
<br/>
<img width="480" alt="locality diagram 8 layers" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/4aa623b4-4394-45c3-b79b-72f0e167d7a9">
<br/>

- How should intensity be accurately visualized (color, opacity, depth etc.)?
- Apply upwards and downwards for a cell?
- Sequence of nested diagrams?

python script:
<br/>
[public/scripts/gen_locality_diagram.py](https://github.com/tboie/universal_phreak_generator/blob/main/public/scripts/gen_locality_diagram.py)
<br/>
<br/>

Locality Trace Diagram (revise?):
<br/>
<img width="480" alt="locality trace diagram" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/f1a09742-a2f1-476e-a48c-1af41ba9af05">
<br/>
<br/>

## Nothing to Something Sequence

### Proof and Definition of Minimal Scaling Parts

Stuctures of System Scales:

Scale 1 (1x1): Points
Scale 2 (2x2): Points, Lines, Triangles
Scale 3 (3x3): Circles

Specify a Grid Cell:

```
1
```

Scale the Grid to 2x2 allowing area for parts?

```
10
00
```

A Line defines direction?

```
11
00

10
10

10
01

...
```

A Triangle is minimal form of area?

```
11
10
```

Expanding the triangle creates the 2/3 ruleset for a minimal, stable, complete, scaled cell from it's parts?

```
11
11
```
Does the following sequence pattern emerge from locality diagrams/trace diagrams starting from 1 "on" cell?

```
expanding rotating square boundary sample sequence:

0 0 0
0 1 0
0 0 0

0 0 0
0 1 0
0 0 0


0 1 0
1 0 1
0 1 0

1 1 1
1 0 1
1 1 1

0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0

1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1

...
```

<br/>

Locality diagrams of first 3 sequence forms:

Are these "Processing States" of the Primary Mechanism?

<br/><br/>
Cell Data Map?:
<br/>
![locality_diagram_8_point](https://github.com/tboie/universal_phreak_generator/assets/26150152/8eb0a8ac-6cda-43d1-8e6a-0b6913dca6d4)
<br/><br/>
Initiated State?:
<br/>
![locality_diagram_8_dead](https://github.com/tboie/universal_phreak_generator/assets/26150152/c7d89f6c-6555-47f0-b95f-f6987fc5b9dd)
<br/><br/>
Expanding State?:
<br/>
![locality_diagram_8_o](https://github.com/tboie/universal_phreak_generator/assets/26150152/f4e88433-97a0-457d-9711-69f39b3158bf)
<br/><br/>
Active State? (1st layer sequence):
<br/>
![locality_diagram_8 active](https://github.com/user-attachments/assets/c363eb98-db27-4058-9e4e-ea601522f7ed)
<br/><br/>
Inactive State?:
<br/>
![locality_diagram_8 inactive](https://github.com/user-attachments/assets/f42dfe29-243c-4f41-92a3-21bdc0d954a8)
<br/><br/>
Activating State?:
<br/>
![locality_diagram_8 activating](https://github.com/user-attachments/assets/5238b100-eae3-41fd-a969-e6987ae8b347)
<br/><br/>
TODO?:
<br/>
Scaled single cell?
<br/><br/>
Triangles?
```
ex)

010
000
101
```

<br/><br/>

#### Mechanism

Mechanisms are scaling foundational forms?

Demo of Sequence:

<br/>

![gen](https://github.com/tboie/universal_phreak_generator/assets/26150152/3aa9e4dd-7ac1-4ee0-859d-5cba94b0bce0)

note: demo is missing a point from beginning of sequence

<br/>

Demo of 400 generations:
<br/>
![demo sequence 400 gens](https://github.com/tboie/universal_phreak_generator/assets/26150152/0e39819b-89cc-42a1-b379-22e458bd5a36)

#### Primary Mechanism

Layered Sequence Concept:
<br/>
<img width="600" alt="" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/375901f0-900d-4fb9-aa66-f1906973229f">
<br/>
<br/>
#### 32 layer demo:
<br/>
<img width="600" alt="" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/6978e0fe-0bf8-4281-902b-c0b27300a66e">

<br/>
<br/>

- Outwards version = Mechanism?

- Triangle Mechanism?
  - Scaling rotating 3 points since a triangle is not complete?

- Does every "Iniated State(Tub)" pattern start a new layer and sequence?
- Does the sequence continuously add for each generation while "Iniated State(Tub)" exists?
  - No because "Nothing to Something Sequence" is exclusively generated by system totality (perfect rotation)?
  - What about Tubs located in the center such as layer 25?
  - No because different from Nothing to Something sequence (2 rotations inside center cell)?

<br/>

- All information contained in cell?
- Reaction resembles locality diagrams? (significance if true? data matches data?) 
- Cell form scales?
- Scale increases towards resulting outer boundary?
- Single "on" cell is specific case of system?
- Nothing is something?
- Number of Locality Diagram layers for each layer = layer number?
- Include expanding base layer in demo?
- How does data process vertically?
  - Is there form like objects/patterns in layered geometry?
  - Tubes from Expanding Boundary?
  - Other methodologies to learn about the cell expansion/structure?
  - ex) results from tesselating "expanding/initiated state" patterns from locality diagrams?
    - structure to mass produce Tub (Initiated State) = interesting?
  - can parts/areas/states of the expanding cell be modeled independently?
- Scaling tile perimeter?
- [Demo script](https://github.com/tboie/universal_phreak_generator/blob/main/public/scripts/sequences/gen_rotating_square_layers.py)
- [Layered sequence web demo](https://github.com/tboie/universal_phreak_generator/tree/main/public/scripts/media/html_layers)
- [Readme for scripts info](https://github.com/tboie/universal_phreak_generator/blob/main/public/scripts/readme.txt)

<br/>
<br/>

## Tiles

TODO: tile common patterns and all matrix combinations?

Tile = form?

Tesselated tiles display scaled pattern information? (pattern is squared)

Tesselation = scaled reaction of form?

Does this method relate to Rotating Cell and Boundary? Scaling structure of system? Horizontal/Vertical pattern relation? 

A block is 4 quadrants? A blinker rotates 90 degrees? A tile combines concepts of the 2 most common patterns.

Tiling Scripts:

[generate tiled tesselations](https://github.com/tboie/universal_phreak_generator/blob/main/public/scripts/gen_tile_seq.py)
<br/>
[graph reaction size](https://github.com/tboie/universal_phreak_generator/blob/main/public/scripts/gen_graph.py)
<br/>

<br/>

The 4 glider spiral reaction might contain design information.

<img width="450" alt="4 Glider Spiral" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/22e031ae-8069-41a4-b765-c2eb8fc6b2ad">

<br/>

### LIGHTING UP THE AREA?:

<img width="120" alt="area light tile" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/ca715375-ccb1-4410-8c9d-014c3574e9f8">
<br/>
<img width="450" alt="area light" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/232e3317-78cf-4e66-ad98-113216a581dd"/>

```
x = 24, y = 24, rule = B3/S23
4bo5bo5bo5bo$obo3bobo3bobo3bobo$2b3o3b3o3b3o3b3o$b3o3b3o3b3o3b3o$3bobo
3bobo3bobo3bobo$bo5bo5bo5bo$4bo5bo5bo5bo$obo3bobo3bobo3bobo$2b3o3b3o3b
3o3b3o$b3o3b3o3b3o3b3o$3bobo3bobo3bobo3bobo$bo5bo5bo5bo$4bo5bo5bo5bo$o
bo3bobo3bobo3bobo$2b3o3b3o3b3o3b3o$b3o3b3o3b3o3b3o$3bobo3bobo3bobo3bob
o$bo5bo5bo5bo$4bo5bo5bo5bo$obo3bobo3bobo3bobo$2b3o3b3o3b3o3b3o$b3o3b3o
3b3o3b3o$3bobo3bobo3bobo3bobo$bo5bo5bo5bo!
```

<br/>

#### Solid State/Empty Border Collapse Version

<img width="377" alt="area light collapse" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/e6f03f4b-09d4-49bb-9121-10fbc3d46c98">

<br/>

```
x = 20, y = 20, rule = B3/S23
2bo5bo5bo$5bo5bo5bo$b2ob2ob2ob2ob2ob2obo$2bo5bo5bo$5bo5bo5bo$ob2ob2ob
2ob2ob2ob2o$2bo5bo5bo$5bo5bo5bo$b2ob2ob2ob2ob2ob2obo$2bo5bo5bo$5bo5bo
5bo$ob2ob2ob2ob2ob2ob2o$2bo5bo5bo$5bo5bo5bo$b2ob2ob2ob2ob2ob2obo$2bo5b
o5bo$5bo5bo5bo$ob2ob2ob2ob2ob2ob2o$2bo5bo5bo$5bo5bo5bo!
```

<br/>

### Spiral?

Notice opposing directions of spiral patterns?

<img width="356" alt="spacetimestop-tile" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/087dcb96-d61b-4f07-b041-e6af7eb88400">

```
x = 20, y = 20, rule = B3/S23
3b5o5b5o$2bo4bo4bo4bo$3o4b2ob3o4b2o$o3bo4b2o3bo4bo$o3b3o2b2o3b3o2bo$o
2b3o3b2o2b3o3bo$o4bo3b2o4bo3bo$b2o4b3ob2o4b3o$2bo4bo4bo4bo$2b5o5b5o$3b
5o5b5o$2bo4bo4bo4bo$3o4b2ob3o4b2o$o3bo4b2o3bo4bo$o3b3o2b2o3b3o2bo$o2b
3o3b2o2b3o3bo$o4bo3b2o4bo3bo$b2o4b3ob2o4b3o$2bo4bo4bo4bo$2b5o5b5o!
```

![Screen Recording 2023-08-03 at 11 26 37 AM](https://github.com/tboie/universal_phreak_generator/assets/26150152/97605187-ee54-481d-9e28-f235e18be39d)

<br/>

### Structured Collapse

Simplified Tile:

<img width="338" alt="structured collapse tile" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/56b1289d-38c5-45ed-98c4-097d494ac02f">

Tiled Reaction Example:

![Screen Recording 2023-07-31 at 5 35 47 PM](https://github.com/tboie/universal_phreak_generator/assets/26150152/2464a93a-d9d7-45f2-a100-e7b90e4a06d0)

[medium scale .rle file](https://github.com/tboie/universal_phreak_generator/blob/main/public/structured_collapse_md.rle)

Larger Scale Tiled Reaction Example:

![Screen Recording 2023-08-01 at 9 49 48 AM](https://github.com/tboie/universal_phreak_generator/assets/26150152/4f808299-eb0b-48e1-a383-47c3becd2c84)

[large scale .rle file](https://github.com/tboie/universal_phreak_generator/blob/main/public/structured_collapse_lg.rle)

<br/>

### Another Banger

<img width="350" alt="Screen Shot 2023-08-08 at 9 22 25 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/29ed2d35-19c3-477f-97bc-6e5f2ef839d0">

```
x = 20, y = 20, rule = B3/S23
b3obo5b3obo$7bobo7bobo$bobobo3bobobobo3bo$3b5obo3b5obo$ob5o3bob5o$3b5o
bo3b5obo$ob5o3bob5o$o3bobobobo3bobobo$obo7bobo$4bob3o5bob3o$b3obo5b3ob
o$7bobo7bobo$bobobo3bobobobo3bo$3b5obo3b5obo$ob5o3bob5o$3b5obo3b5obo$o
b5o3bob5o$o3bobobobo3bobobo$obo7bobo$4bob3o5bob3o!
```

<br/>

### More Bang

<img width="340" alt="electro-noise-base" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/1b6f3ec1-cc1b-4373-8ca1-12768e7bdc25">

```
x = 20, y = 20, rule = B3/S23
3bo9bo$2b3o7b3o$2bobo2b2o3bobo2b2o$3b4ob2o3b4ob2o$3bo2b3o4bo2b3o$b3o2b
o4b3o2bo$2ob4o3b2ob4o$b2o2bobo3b2o2bobo$5b3o7b3o$6bo9bo$3bo9bo$2b3o7b
3o$2bobo2b2o3bobo2b2o$3b4ob2o3b4ob2o$3bo2b3o4bo2b3o$b3o2bo4b3o2bo$2ob
4o3b2ob4o$b2o2bobo3b2o2bobo$5b3o7b3o$6bo9bo!
```

![Screen Recording 2023-08-04 at 2 05 09 PM](https://github.com/tboie/universal_phreak_generator/assets/26150152/ecb7dd1e-6abf-44b1-85a4-6731ad862f80)

[electronoiserip_lg.rle](https://github.com/tboie/universal_phreak_generator/blob/main/public/electronoiserip_lg.rle)

<br/>

### Cancellation

<img width="288" alt="spin mechanism tile" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/aa7e0d67-15f3-4240-829d-092b94d9f6b7">

```
x = 16, y = 16, rule = B3/S23
2b2o6b2o$bo2b3o2bo2b3o$bobo3bobobo3bo$bo3bobobo3bobo$obo3bobobo3bo$o3b
obobo3bobo$b3o2bo2b3o2bo$4b2o6b2o$2b2o6b2o$bo2b3o2bo2b3o$bobo3bobobo3b
o$bo3bobobo3bobo$obo3bobobo3bo$o3bobobo3bobo$b3o2bo2b3o2bo$4b2o6b2o!
```

Note: At this point in experiments, 1 beehive in each corner remain when all other matter is "cancelled". Also, scaling the tileset produces the same reaction.

![Screen Recording 2023-08-04 at 9 20 13 AM](https://github.com/tboie/universal_phreak_generator/assets/26150152/ada9b19d-6816-475f-8734-9843a001ad22)

3x3 tile tesselation results in outwards gliders.

Is there a system spin mechanism/value? Is it possible to visualize system spin mechanism/value? Would it be 1 bit in each corner as a base value?

<br/>

### Reactions going outward

<img width="322" alt="Screen Shot 2023-08-08 at 7 04 08 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/e9328c58-71eb-4ae2-bb4c-76fcb47fa9d5">

```
x = 16, y = 16, rule = B3/S23
b2o3bo2b2o3bo$o2b3ob2o2b3obo$b3obobob3obobo$bo3b2o2bo3b2o$b2o3bo2b2o3b
o$obob3obobob3o$ob3o2b2ob3o2bo$bo3b2o2bo3b2o$b2o3bo2b2o3bo$o2b3ob2o2b
3obo$b3obobob3obobo$bo3b2o2bo3b2o$b2o3bo2b2o3bo$obob3obobob3o$ob3o2b2o
b3o2bo$bo3b2o2bo3b2o!
```

![Screen Recording 2023-08-08 at 7 02 42 AM](https://github.com/tboie/universal_phreak_generator/assets/26150152/e8270a3f-00c6-4f5d-a67f-56a75da5c934)

<img width="259" alt="Screen Shot 2023-08-15 at 12 53 16 PM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/151c27bf-b5aa-4d26-ab56-e951e5b31f7b">

```
x = 14, y = 14, rule = B3/S23
b2o2bo2b2o2bo$o2b2ob2o2b2obo$b2obobob2obobo$bo3bo2bo3bo$obob2obobob2o$
ob2o2b2ob2o2bo$bo2b2o2bo2b2o$b2o2bo2b2o2bo$o2b2ob2o2b2obo$b2obobob2obo
bo$bo3bo2bo3bo$obob2obobob2o$ob2o2b2ob2o2bo$bo2b2o2bo2b2o!
```

<br/>

### Reaction going inwards

<img width="292" alt="Screen Shot 2023-08-15 at 2 23 43 PM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/abcb9720-50a3-4c6d-83a7-7fcd2834ff81">

```
x = 16, y = 16, rule = B3/S23
6ob7obo$b7ob7o$16o$16o$16o$16o$7ob7o$ob7ob6o$6ob7obo$b7ob7o$16o$16o$
16o$16o$7ob7o$ob7ob6o!
```

<br/>

### Reaction going inward and outward

<img width="289" alt="Screen Shot 2023-08-08 at 9 43 21 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/3d22ea4e-a33f-4498-aac2-50f419eae7aa">

```
x = 16, y = 16, rule = B3/S23
b2o3bo2b2o3bo$o2b3ob2o2b3obo$b2ob2obob2ob2obo$b2o3bo2b2o3bo$bo3b2o2bo
3b2o$ob2ob2obob2ob2o$ob3o2b2ob3o2bo$bo3b2o2bo3b2o$b2o3bo2b2o3bo$o2b3ob
2o2b3obo$b2ob2obob2ob2obo$b2o3bo2b2o3bo$bo3b2o2bo3b2o$ob2ob2obob2ob2o$
ob3o2b2ob3o2bo$bo3b2o2bo3b2o!
```

![Screen Recording 2023-08-08 at 9 41 15 AM](https://github.com/tboie/universal_phreak_generator/assets/26150152/728e873f-c08d-42ca-b226-67db012d43ca)

<br/>

### Oscillating Pattern Reaction

<img width="195" alt="Screen Shot 2023-08-16 at 9 54 58 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/ed7758af-8e37-4a2e-8c12-a9245b03409f">

```
x = 10, y = 10, rule = B3/S23
3bo4bo$4ob4o$bobo2bobo$b4ob4o$bo4bo$3bo4bo$4ob4o$bobo2bobo$b4ob4o$bo4b
o!
```

<br/>

### Circular results?

<img width="228" alt="circular result" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/ef56ffe6-bc6a-4f44-993e-f9cbe5660c1d">

```
x = 12, y = 12, rule = B3/S23
3o2b4o2bo$bo2b2obo2b2o$2b2obo2b2obo$ob2o2bob2o$2o2bob2o2bo$o2b4o2b3o$
3o2b4o2bo$bo2b2obo2b2o$2b2obo2b2obo$ob2o2bob2o$2o2bob2o2bo$o2b4o2b3o!
```

Same result?

<img width="225" alt="circular result base" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/573498a1-c3ab-4e2e-bd73-6aeb4bfd941d">

```
x = 12, y = 12, rule = B3/S23
2ob5ob3o$ob2ob2ob2obo$5ob5o$b5ob5o$ob2ob2ob2obo$3ob5ob2o$2ob5ob3o$ob2o
b2ob2obo$5ob5o$b5ob5o$ob2ob2ob2obo$3ob5ob2o!
```

Same result?

<img width="225" alt="circular result base 3" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/4ba74200-d208-4210-9b2a-bd8b89119c84">

```
x = 12, y = 12, rule = B3/S23
2obob3obobo$2b2obo2b2obo$5ob5o$b5ob5o$ob2o2bob2o$obob3obob2o$2obob3obo
bo$2b2obo2b2obo$5ob5o$b5ob5o$ob2o2bob2o$obob3obob2o!
```

<br/>

### Smallest Outward Glider Tiles

Base form at which information travels in all directions indefinitely?

- 10x10

<img width="197" alt="outwards-glider" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/89e14d7c-4641-4f31-9c03-da77ead1585d">

```
x = 10, y = 10, rule = B3/S23
3b2ob2o$2bo4bo$3o4b2o$o3bo4bo$6bo2bo$o2bo$o4bo3bo$b2o4b3o$2bo4bo$2b2ob
2o!
```

- 8x8
- reaction result not constant
- reaction at tesselation size 256x256 is interesting
  - inner gliders movement change
  - octagon to square to octagon?

Note: are tileset sizes 256/512 significant?

<img width="160" alt="Screen Shot 2023-08-23 at 12 51 32 PM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/5c2c34cc-7ef2-41ba-9f17-eeae60f5ec77">

```
x = 8, y = 8, rule = B3/S23
2obo3bo$bob2ob2o$2b2obo$bo3b3o$3o3bo$2bob2o$2ob2obo$o3bob2o!
```

<br/>

### Towards Infinity Tile

<img width="293" alt="towards infinity tile" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/823de780-c931-49c2-aa5c-a4ee92cb86a8">

```
x = 34, y = 34, rule = B3/S23
23bo$22bobo$22bobo$23bo$6bo$5bobo10b2o7b2o$5bobo9bo2bo5bo2bo$6bo11b2o
7b2o2$b2o7b2o11bo$o2bo5bo2bo9bobo$b2o7b2o10bobo$15b2ob2o3bo$6bo7bo4bo$
5bobo4b3o4b2o$5bobo4bo3bo4bo$6bo11bo2bo$12bo2bo11bo$12bo4bo3bo4bobo$
13b2o4b3o4bobo$14bo4bo7bo$10bo3b2ob2o$9bobo10b2o7b2o$9bobo9bo2bo5bo2bo
$10bo11b2o7b2o2$5b2o7b2o11bo$4bo2bo5bo2bo9bobo$5b2o7b2o10bobo$27bo$10b
o$9bobo$9bobo$10bo!
```

<br/>

#### Extensive Beginnings Concept:

- Medium weight spaceships emerge

<img width="308" alt="towards infinity tile extended" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/111d0b8f-905b-4c17-bd4c-174cc395354c">

```
x = 70, y = 70, rule = B3/S23
23bo$22bobo$22bobo$23bo2$18b2o7b2o$17bo2bo5bo2bo$18b2o7b2o$54bo$14bo8b
o8bo20bobo$13bobo6bobo6bobo19bobo$13bobo6bobo6bobo20bo$14bo8bo8bo$49b
2o7b2o$9b2o7b2o7b2o7b2o10bo2bo5bo2bo$8bo2bo5bo2bo5bo2bo5bo2bo10b2o7b2o
$9b2o7b2o7b2o7b2o$54bo8bo$14bo17bo8bo11bobo6bobo$13bobo15bobo6bobo10bo
bo6bobo$13bobo15bobo6bobo11bo8bo$14bo17bo8bo$24bo33b2o7b2o$23bobo10b2o
7b2o10bo2bo5bo2bo$23bobo9bo2bo5bo2bo10b2o7b2o$24bo11b2o7b2o$54bo8bo$
19b2o7b2o11bo11bobo6bobo$18bo2bo5bo2bo9bobo10bobo6bobo$19b2o7b2o10bobo
11bo8bo$33b2ob2o3bo$15bo8bo7bo4bo11b2o7b2o$14bobo6bobo4b3o4b2o9bo2bo5b
o2bo$14bobo6bobo4bo3bo4bo9b2o7b2o$15bo8bo11bo2bo$30bo2bo11bo8bo$10b2o
7b2o9bo4bo3bo4bobo6bobo$9bo2bo5bo2bo9b2o4b3o4bobo6bobo$10b2o7b2o11bo4b
o7bo8bo$28bo3b2ob2o$6bo8bo11bobo10b2o7b2o$5bobo6bobo10bobo9bo2bo5bo2bo
$5bobo6bobo11bo11b2o7b2o$6bo8bo$23b2o7b2o11bo$b2o7b2o10bo2bo5bo2bo9bob
o$o2bo5bo2bo10b2o7b2o10bobo$b2o7b2o33bo$28bo8bo17bo$6bo8bo11bobo6bobo
15bobo$5bobo6bobo10bobo6bobo15bobo$5bobo6bobo11bo8bo17bo$6bo8bo$32b2o
7b2o7b2o7b2o$10b2o7b2o10bo2bo5bo2bo5bo2bo5bo2bo$9bo2bo5bo2bo10b2o7b2o
7b2o7b2o$10b2o7b2o$37bo8bo8bo$15bo20bobo6bobo6bobo$14bobo19bobo6bobo6b
obo$14bobo20bo8bo8bo$15bo$41b2o7b2o$40bo2bo5bo2bo$41b2o7b2o2$46bo$45bo
bo$45bobo$46bo!
```

<br/>

### Infinite Angle

- tile design is the space between a particle and a side
- eternal gliders emerge from the center of a square after it is fully lit

<img width="129" alt="infinite reflections" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/27e58374-19c6-460b-8264-9fc981a62fb4">

```
x = 60, y = 60, rule = B3/S23
2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$obo3bobo3bobo3bobo
3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b
4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo3bobo3bobo3bobo3bo
bo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bo
bo$2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$obo3bobo3bobo3bo
bo3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o
2b4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo3bobo3bobo3bobo
3bobo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo
3bobo$2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$obo3bobo3bobo
3bobo3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b
4o2b4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo3bobo3bobo3bob
o3bobo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bob
o3bobo$2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$obo3bobo3bob
o3bobo3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o
2b4o2b4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo3bobo3bobo3b
obo3bobo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3b
obo3bobo$2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$obo3bobo3b
obo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b
4o2b4o2b4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo3bobo3bobo
3bobo3bobo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo
3bobo3bobo$2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$obo3bobo
3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o2b4o2b4o
2b4o2b4o2b4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo3bobo3bo
bo3bobo3bobo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo3bobo3bo
bo3bobo3bobo$2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$obo3bo
bo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o2b4o2b
4o2b4o2b4o2b4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo3bobo
3bobo3bobo3bobo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo3bobo
3bobo3bobo3bobo$2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$obo
3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o2b4o
2b4o2b4o2b4o2b4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo3bob
o3bobo3bobo3bobo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo3bob
o3bobo3bobo3bobo$2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$ob
o3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o2b
4o2b4o2b4o2b4o2b4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo3b
obo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo3b
obo3bobo3bobo3bobo$2bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$
obo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$2b4o2b4o2b4o2b4o2b4o
2b4o2b4o2b4o2b4o2b4o$4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o2b4o$3bobo3bobo
3bobo3bobo3bobo3bobo3bobo3bobo3bobo3bobo$bobo3bobo3bobo3bobo3bobo3bobo
3bobo3bobo3bobo3bobo!
```

<br/>

### Minimal tile system deployment

- system composed of at least 2 types

<img width="128" alt="minimal system deployment" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/6e4bfd88-adc7-4baa-9116-75b2fffc5ecf">

```
x = 6, y = 6, rule = B3/S23
3o2bo$b2ob2o$4b2o$2o$2ob2o$o2b3o!
```

Same result?

<img width="127" alt="minimal system deployment 2" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/f171ff31-2421-42a3-ba51-7273e44278de">

```
x = 6, y = 6, rule = B3/S23
3o2bo$b2ob2o$2b4o$4o$2ob2o$o2b3o!
```

<br/>
<br/>


## System energy calculations

[Code in App.tsx](https://github.com/tboie/universal_phreak_generator/blob/main/src/App.tsx#L198)

- Alive energy uses alive cells
- Dead energy uses dead cells within a bounding box around min/max of alive cell x/y in system

  - Calculate another "category" for dead cells adjacent to alive cells?
    - Adjacent Dead Cell ADPV = Total Connected Alive Cells / 8 ?

- System energy changes create waveform?

<br/>
<br/>

## Phreak Phormulas

<img width="500" alt="Phreak Phormula" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/a3c7dd18-6ea3-4db9-9d50-f7504c11d638">
<br/>
<img width="350" alt="Phreak Phormula example 1" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/14e497cb-e473-4b72-aa12-057b2963d967">
<br/>
<img width="350" alt="Phreak Phormula example 2" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/8685a79d-8af1-4df3-81ae-e506a87d57e4">

<br/>

more initial state designs (ring version, fibonnaci spiral) found here:
[src/App.tsx](https://github.com/tboie/universal_phreak_generator/blob/main/src/App.tsx)

<br/>

## Minimal Creation Concepts

A cell exists. Define area.

<img width="52" alt="define cell" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/3b935aa7-3581-4223-a24a-cfc70cae7cd9">

<br/><br/>

Define pieces using last generation of sequence.

<img width="177" alt="define cell pieces" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/5ae1c7c7-ca5d-46af-9f68-1c2f5b01f163">

<br/><br/>

Define areas from pieces.

<img width="304" alt="Screen Shot 2023-11-22 at 11 45 10 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/df5fe56d-49ef-4980-85ce-0f3f53ad0717">

<br/><br/>

Result:

<img width="304" alt="Screen Shot 2023-11-22 at 11 45 50 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/87b9b685-52f8-4ba4-b4e0-96220a20a4c8">

<br/><br/>

Expansion by adding defined pieces:

<img width="304" alt="adding defined pieces" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/a8a9546c-36b8-42de-9c67-c2d876fa875e">

```
x = 27, y = 27, rule = B3/S23
12b3o$12bobo$12bobo$12bobo$12b3o$12bobo$12bobo$12bobo$12b3o$12bobo$12b
obo$12bobo$27o$o3bo3bo3bobo3bo3bo3bo$27o$12bobo$12bobo$12bobo$12b3o$
12bobo$12bobo$12bobo$12b3o$12bobo$12bobo$12bobo$12b3o!
```

<br/><br/>

Combining pieces and areas:

<img width="304" alt="minimal creation combination" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/f1d8f806-0d8e-48c2-824d-ab9f9162998a">

<br/><br/>

Define combination:

<img width="304" alt="minimal creation define system" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/f0fb4950-1eb1-4754-a7c5-bd579faa91c1">

```
x = 31, y = 31, rule = B3/S23
31o$o29bo$ob27obo$obo3bo3bo3bobo3bo3bo3bobo$obo3bo3bo3bobo3bo3bo3bobo$
obo3bo3bo3bobo3bo3bo3bobo$ob27obo$obo3bo3bo3bobo3bo3bo3bobo$obo3bo3bo
3bobo3bo3bo3bobo$obo3bo3bo3bobo3bo3bo3bobo$ob27obo$obo3bo3bo3bobo3bo3b
o3bobo$obo3bo3bo3bobo3bo3bo3bobo$obo3bo3bo3bobo3bo3bo3bobo$ob27obo$obo
3bo3bo3bobo3bo3bo3bobo$ob27obo$obo3bo3bo3bobo3bo3bo3bobo$obo3bo3bo3bob
o3bo3bo3bobo$obo3bo3bo3bobo3bo3bo3bobo$ob27obo$obo3bo3bo3bobo3bo3bo3bo
bo$obo3bo3bo3bobo3bo3bo3bobo$obo3bo3bo3bobo3bo3bo3bobo$ob27obo$obo3bo
3bo3bobo3bo3bo3bobo$obo3bo3bo3bobo3bo3bo3bobo$obo3bo3bo3bobo3bo3bo3bob
o$ob27obo$o29bo$31o!
```

<br/><br/>

Layering each defined combination of pieces and areas:

<img width="304" alt="minimal creation layered" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/7c0d201d-e78b-42fd-b62c-1bfc94319cf7">

```
x = 39, y = 39, rule = B3/S23
39o$o37bo$ob35obo$obo3bo3bo3bo3bobo3bo3bo3bo3bobo$obob31obobo$obobobo
3bo3bo3bobo3bo3bo3bobobobo$ob35obo$obobobo3bo3bo3bobo3bo3bo3bobobobo$o
bobobob23obobobobo$obobobobobo3bo3bobo3bo3bobobobobobo$ob35obo$obobobo
bobo3bo3bobo3bo3bobobobobobo$obobobobobob15obobobobobobo$obobobobobobo
bo3bobo3bobobobobobobobo$ob35obo$obobobobobobobo3bobo3bobobobobobobobo
$obobobobobobobo3bobo3bobobobobobobobo$obobobobobobobo3bobo3bobobobobo
bobobo$ob35obo$obobobobobobobo3bobo3bobobobobobobobo$ob35obo$obobobobo
bobobo3bobo3bobobobobobobobo$obobobobobobobo3bobo3bobobobobobobobo$obo
bobobobobobo3bobo3bobobobobobobobo$ob35obo$obobobobobobobo3bobo3bobobo
bobobobobo$obobobobobob15obobobobobobo$obobobobobo3bo3bobo3bo3bobobobo
bobo$ob35obo$obobobobobo3bo3bobo3bo3bobobobobobo$obobobob23obobobobo$o
bobobo3bo3bo3bobo3bo3bo3bobobobo$ob35obo$obobobo3bo3bo3bobo3bo3bo3bobo
bobo$obob31obobo$obo3bo3bo3bo3bobo3bo3bo3bo3bobo$ob35obo$o37bo$39o!

```

<br/><br/>

## Blinker with middle at 0,0 has bounding box dead energy change floating point difference?

```
  1.0000000000000036
- 0.9999999999999964
= 0.000000000000007 (7x10^-15 femto)
```

```
  1
/ 0.000000000000007
= 142857142857142.857142857142857
```

Defining bounding box of blinker creates a pulsar:

- https://conwaylife.com/wiki/Pulsar
- 3x3 center is interesting?

<br/>

## Significance of system ruleset numbers 2 and 3?

- triangle?

- connections of 2 in a neighborhood length of 3?

<br/>

## 9 cell neighborhood combinations produce 9 most common patterns

- https://catagolue.hatsya.com/statistics
- 1 xs4_33 (Block) 1641635518161410
- 2 xp2_7 (Blinker) 1524639293713408
- 3 xs6_696 (Beehive) 869945894691485
- 4 xq4_153 (Glider) 467343903744820
- 5 xs7_2596 (Loaf) 256651602436129
- 6 xs5_253 (Boat) 236781408150196
- 7 xs6_356 (Ship) 163492510796214
- 8 xs4_252 (Tub) 51670473427163
- 9 xs8_6996 (Pond) 55336623799705

<br/>
<br/>

## Universal Tile Generator

### _Squared Version_

1.  Assign random bits (rotating 3d cubes?) to _x_ size matrix(s) representing a quadrant
2.  Rotate matrix(s) clockwise for quadrants to form a tile
3.  Goto next generation and check for changes
4.  Scale tiling area
5.  Go to next generation and check for changes
6.  Repeat step 4

- Detect tiles naturally generated at center of reactions?

<br/>

## Universal Border Generator

- random border pattern generator
- variations in corners?

<br/>

## Universal Initial State Generator

Is this still relevant?

- Initial State Design = Layered Shape(s) \* (Universal Tile Generator + Universal Border Generator)

<br/>

## Pattern Balance Technique

- example uses [Unique Father Problem](https://conwaylife.com/wiki/Unique_father_problem)

<img width="700" alt="concept" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/06d05e6a-1baa-4f8b-9880-b3b41d98967d">

1.  X pattern is horizontal
2.  Y pattern is inverted and rotated
3.  Golden Spiral Matrix

Comparing 4 glider spiral reactions to the [Unique Father Problem](https://conwaylife.com/wiki/Unique_father_problem) and Pattern Balance Technique
<br/>
<img width="95" alt="Screen Shot 2023-07-14 at 8 31 30 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/7f5e1520-dc4b-42a2-a4f5-5edd75e6bc0d">
<img width="91" alt="Screen Shot 2023-07-14 at 8 31 22 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/731f0da1-5979-49e0-9ef3-06c9404ec06d">
<img width="89" alt="Screen Shot 2023-07-14 at 8 31 42 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/a3ffb028-15b8-4d26-a30c-458ddc728f9b">
<br/>
<img width="450" alt="Unique Father Problem" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/7c44c22a-fdc0-4385-8bd1-f04713439772">
<br/>
<img width="450" alt="Core Collapse" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/ec861f9f-1220-401f-8d91-f7f0f98f25b0">
<br/><br/>

<br/>

## Simplest combination creating multiple gliders from 1?

<img width="150" alt="multiple gliders from 1" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/cece1393-a0cd-4ba8-8d8e-d55c12aa375d">

```
x = 8, y = 9, rule = B3/S23
4b2o$3bo2bo$4b2o$bo$obo$obo$bo3b2o$5bobo$5bo!
```

<br/>

## Is this glider arrangement possible?

<img width="76" alt="glider arrangement" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/7ee3b9d3-6e63-452c-aba1-713e2f10137d">

<br/><br/>

## Adjacent Differential Points Value?

- Implement visualization?
- Does the value relate to cells with greatest alive/dead energy in system? (distance?)

<img width="480" alt="adpv" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/2a29a356-8746-4d55-9829-8be2035fe234">

<br/><br/>

Dead Cell ADPV = Total Connected Alive Cells / 8 ?

<br/><br/>

## What is geometry of each cell/point?

- pyramid/cone?

## Random note for later: 0.125 sequence is combinationally interesting?

- 0
- 0.125
- 0.25
- 0.375
- 0.5
- 0.625
- 0.75
- 0.875
- 1

<br/>
<br/>

## Neighborhood Fibonnaci Sequence

```
301
3 1
322
```

```
011
3 2
332
```

The following:

```
100
101
111
```

Produces infinite gliders matching corner values:

```
133
1 3
220
```

## Neighborhood Time Differentials

Time = 0
<br/>
<img width="420" alt="neiborhood time diff 0" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/c2d8d724-6e08-4506-99f9-356e7746aef0">

<br/>

Time = 1
<br/>
<img width="420" alt="neighborhood time diff 1" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/607498d5-722e-4055-a383-bf9e474557b2">

<br/>

More concepts in code experiments at [src/App.tsx](https://github.com/tboie/universal_phreak_generator/blob/main/src/App.tsx)

<br/>
<br/>

## Rotating cells around scaling cell

TODO: move surrounding cells outwards by 1 so there is a boundary of no information between the center cell? (neighboring cells have information in locality diagrams)

```
1 0 0 0 1
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0 
1 0 0 0 1

0 1 0 0 0
0 0 0 0 1
0 0 1 0 0
1 0 0 0 0 
0 0 0 1 0

...


1 0 0 0 0 1
0 0 0 0 0 0
0 0 1 1 0 0
0 0 1 1 0 0
0 0 0 0 0 0
1 0 0 0 0 1

0 1 0 0 0 0
0 0 0 0 0 1
0 0 1 1 0 0
0 0 1 1 0 0
1 0 0 0 0 0
0 0 0 0 1 0

...


1 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 1 1 1 0 0
0 0 1 1 1 0 0
0 0 1 1 1 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 1

0 1 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 1 1 0 0
0 0 1 1 1 0 0
0 0 1 1 1 0 0
1 0 0 0 0 0 0
0 0 0 0 0 1 0

....
```

## Triangle and 1 dimensional automata
- Proof of scaling functionality?
  

