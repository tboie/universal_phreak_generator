# Conway Game of Life Experiments
## A spiraling collection of virtual measurements

### Notes on https://conwaylife.com/wiki/Unique_father_problem

<img width="700" alt="concept" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/06d05e6a-1baa-4f8b-9880-b3b41d98967d">

1.  X pattern is horizontal
2.  Y pattern is inverted and rotated
3.  Golden Spiral Matrix

<br/>

## Core Collapse?

<img width="450" alt="core collapse" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/9b4fb570-ef1d-4f51-a268-31bb4f510c16">

<img width="450" alt="core collapse pattern" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/3480ffbf-551b-4f2d-9b91-7ebadad94e04">

```
x = 28, y = 22, rule = B3/S23
o2b4o2b4o2b4o2b4o2bo$b2o2bob2o2bob2o2bob2o2bob2o$b2obo2b2obo2b2obo2b2o
bo2b2o$o2b4o2b4o2b4o2b4o2bo$2obo2b2obo2b2obo2b2obo2b2obo$ob2o2bob2o2b
ob2o2bob2o2bob2o$o2b4o2b4o2b4o2b4o2bo$b2o2bob2o2bob2o2bob2o2bob2o$b2o
bo2b2obo2b2obo2b2obo2b2o$o2b4o2b4o2b4o2b4o2bo$2obo2b2obo2b2obo2b2obo2b
2obo$ob2o2bob2o2bob2o2bob2o2bob2o$o2b4o2b4o2b4o2b4o2bo$b2o2bob2o2bob2o
2bob2o2bob2o$b2obo2b2obo2b2obo2b2obo2b2o$o2b4o2b4o2b4o2b4o2bo$2obo2b2o
bo2b2obo2b2obo2b2obo$ob2o2bob2o2bob2o2bob2o2bob2o$o2b4o2b4o2b4o2b4o2b
o$b2o2bob2o2bob2o2bob2o2bob2o$b2obo2b2obo2b2obo2b2obo2b2o$o2b4o2b4o2b
4o2b4o2bo!
```

<br/>

## Composition?

_Mathematical structure might form from foundational patterns at times visible and not (rotated/inverted/scaled)?_
<br/><br/><br/>

The 4 glider spiral reaction might contain design information.

<img width="450" alt="4 Glider Spiral" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/22e031ae-8069-41a4-b765-c2eb8fc6b2ad">

Comparing glider reactions from 2 of the [Family Four](https://conwaylife.com/wiki/Familiar_fours):

- [Traffic Light](https://catagolue.hatsya.com/object/xp2_s01110szw222/b3s23)
- [Honey Farm](https://catagolue.hatsya.com/object/xs24_y1696z2552wgw2552zy1343/b3s23)

Comparing the [Unique Father Problem](https://conwaylife.com/wiki/Unique_father_problem) and Core Collapse:
<br/>
<img width="95" alt="Screen Shot 2023-07-14 at 8 31 30 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/7f5e1520-dc4b-42a2-a4f5-5edd75e6bc0d">
<img width="91" alt="Screen Shot 2023-07-14 at 8 31 22 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/731f0da1-5979-49e0-9ef3-06c9404ec06d">
<img width="89" alt="Screen Shot 2023-07-14 at 8 31 42 AM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/a3ffb028-15b8-4d26-a30c-458ddc728f9b">
<br/>
<img width="450" alt="Unique Father Problem" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/7c44c22a-fdc0-4385-8bd1-f04713439772">
<img width="450" alt="Core Collapse" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/ec861f9f-1220-401f-8d91-f7f0f98f25b0">
<br/><br/>

Another Potential Pattern of Interest:

[Fleet glider synthesis](https://catagolue.hatsya.com/object/xs24_g8o653wggz11wokc321/b3s23) from the [Family Four](https://conwaylife.com/wiki/Familiar_fours) forms the following pattern:

<img width="143" alt="fleet reaction pattern" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/bcf4e1fe-60a3-4b42-ba7f-d1d15ed39375">

<br/>
<br/>

Tiled:
<br/>
<img width="450" alt="Screen Shot 2023-07-15 at 3 48 31 PM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/b8a547f4-d6fb-4c89-8696-ed17dca9d370">
<br/>

2nd Generation produces a texture of [Ponds](https://conwaylife.com/wiki/Pond). _note: photonegative still lifes?_
<br/>
<img width="450" alt="Screen Shot 2023-07-15 at 3 46 17 PM" src="https://github.com/tboie/universal_phreak_generator/assets/26150152/2224904a-5c1f-4052-afda-dedb66e42c6d">

[Blockade](https://catagolue.hatsya.com/object/xs16_0ggydgj3zop1yd11/b3s23) ...
[Bakery](https://catagolue.hatsya.com/object/xs28_g88m952g8gz1218kid221/b3s23) ...

## Universal Tile Generator

### _Squared Version_
1.  Assign random bits to _x_ size matrix representing a quadrant
2.  Rotate matrix clockwise for quadrants 2, 3, and 4 to form a tile
3.  Scale tiling area
4.  Go to next generation and check for changes
5.  Repeat step 3
