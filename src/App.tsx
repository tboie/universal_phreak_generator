import "./App.css";

import { useEffect } from "react";
import { Point, useGameLife } from "react-game-life";

let prevBoard: Point[] = [];

/*** ***/
// Glider Templates
/** ***/

const one = [
  [0, 1, 0, 0, 1, 1, 1],
  [0, 0, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 0, 1],
  [0, 1, 0, 0, 1, 1, 1],
];

const two = [
  [0, 0, 1, 0, 1, 0, 0],
  [1, 0, 1, 0, 1, 0, 1],
  [0, 1, 1, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1],
  [1, 1, 0, 0, 0, 1, 1],
];

const three = [
  [1, 1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 1, 0, 0],
  [0, 1, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 1, 0],
];

const four = [
  [1, 1, 0, 0, 0, 1, 1],
  [1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 0, 1, 1, 0],
  [1, 0, 1, 0, 1, 0, 1],
  [0, 0, 1, 0, 1, 0, 0],
];

const empty = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
];

const g0 = [
  [0, 0, 1],
  [1, 0, 1],
  [0, 1, 1],
];

const g1 = [
  [0, 1, 0],
  [1, 0, 0],
  [1, 1, 1],
];

const g2 = [
  [1, 1, 1],
  [0, 0, 1],
  [0, 1, 0],
];

const g3 = [
  [1, 1, 0],
  [1, 0, 1],
  [1, 0, 0],
];

// return random glider
const rG = () => {
  const i = Math.floor(Math.random() * (3 - 0) + 0);

  if (i === 0) {
    return g0;
  } else if (i === 1) {
    return g1;
  } else if (i === 2) {
    return g2;
  } else {
    return g3;
  }
};

/***  ***/
// Logarithmic spiral functions
/*** ***/

// 2D vectors
const add =
  ([x0, y0]: any) =>
  ([x1, y1]: any) =>
    [x0 + x1, y0 + y1];

const rotate =
  (θ: any) =>
  ([x, y]: any) =>
    [
      Math.round(x * Math.cos(θ) - y * Math.sin(θ)),
      Math.round(x * Math.sin(θ) + y * Math.cos(θ)),
    ];

// Iterables
const fromGen = (g: any) => ({ [Symbol.iterator]: g });
const range = (n: any) => [...Array(n).keys()];
const map = (f: any) => (it: any) =>
  fromGen(function* () {
    for (const v of it) {
      yield f(v);
    }
  });

const spiralOut = (i: any) => {
  const n = Math.floor(i / 2) + 1;
  const leg = range(n).map((x) => [x, 0]);
  const transform = (p: any) => add([n, 0])(rotate(Math.PI / 2)(p));

  return fromGen(function* () {
    yield* leg;
    yield* map(transform)(spiralOut(i + 1));
  });
};

const take = (n: any) => (it: any) =>
  fromGen(function* () {
    for (let v of it) {
      if (--n < 0) break;
      yield v;
    }
  });

//
// App
//
function App() {
  const [game, canvasRef] = useGameLife({
    graphics: {
      board: { zoom: 15 /*2*/, height: 2000, width: 2000 },
      colors: { background: "#000", cell: "#00FF00" },
    },
    //game: { onNextGeneration: oNextGeneration },
  });

  // calculate change in energy
  function oNextGeneration(board: Point[]) {
    let prevDistance = 0;
    prevBoard.forEach((p) => {
      prevDistance += Math.sqrt((0 - p.x) ** 2 + (0 - p.y) ** 2);
    });

    let distance = 0;
    board.forEach((p) => {
      distance += Math.sqrt((0 - p.x) ** 2 + (0 - p.y) ** 2);
    });

    const velocity = board.length - prevBoard.length + 1;
    const energy = (distance - prevDistance + 1) * velocity ** 2;

    console.log(energy);

    prevBoard = [...board];

    return {};
  }

  useEffect(() => {
    if (game) {
      document.addEventListener("click", (event) => {
        console.log(game.getCells());
      });

      game.speedUp(20);

      /* 4 glider spiral base
      const gliders = [
        [g0, g1],
        [g2, g3],
      ];
      */

      /* 16 glider spiral base
      const gliders = [
        [two, one],
        [three, four],
      ];
      */

      /* 16 glider spiral mega pattern
      const gliders = [
        [two, one],
        [three, four],
      ];
      */

      /* 16 glider cross spiral base
      const gliders = [
        [empty, two],
        [three, empty, one],
        [empty, four],
      ];
      */

      /* 2 spiral merge base (same direction) */
      // breaks down to 4 pieces each side (2 osc, 1 glider, 1 still)
      const gliders = [
        [two, one],
        [three, four],
        [one, four],
        [two, three],
      ];

      /* random 4 gliders
      const gliders = [
        [rG(), rG()],
        [rG(), rG()],
      ];
      */

      gliders.forEach((gs, i) => {
        gs.forEach((g, ii) => {
          g.forEach((gRow, gX) => {
            gRow.forEach((gCell, gY) => {
              if (gCell) {
                // +number for spacing
                /* 4 glider spiral base
                game.bornCell({
                  x: i * 4 + gX,
                  y: ii * 4 + gY,
                });
                */
                /* 16 glider spiral base
                game.bornCell({ x: ii * 8 + gX, y: i * 8 + gY });
                */
                /* 16 glider spiral mega patterne
                game.bornCell({ x: ii * 111 + gX, y: i * 111 + gY });
                */
                /* 16 glider cross spiral base
                game.bornCell({ x: ii * 8 + gX, y: i * 8 + gY });
                */
                /* 2 spiral merge base */
                game.bornCell({ x: ii * 8 + gX, y: i * 8 + gY });
              }
            });
          });
        });
      });

      /* golden spiral probabilities
      // TODO: lol

      const cells = 5112;
      const points = [...take(cells)(spiralOut(0))];

      const rand = (g: number) => {
        const percent = 100 / g;
        const prob = percent / 100;
        const d = Math.random();

        if (d < prob) {
          return true;
        } else {
          return false;
        }
      };

      points.forEach((p, i) => {

        /* lorgarithmic spiral decay algorithm
        const prob = (100 - (100 / cells) * i) / 100;
        const d = Math.random();

        if (d < prob) {
          game.bornCell({ x: p[0], y: p[1] }); // Spawn cell
        }
        */

      /* golden spiral region probabilities
        const x = p[0];
        const y = p[1];

        console.log(p);

        // 8
        if (x >= -8 && x < 8 && y < 8 && y >= -8) {
          if (rand(8)) {
            game.bornCell({ x: x, y: y }); // Spawn cell
          }
        }
        // 21
        if (
          (x >= -34 && x < -13 && y >= 0 && y < 21) ||
          (x >= -21 && x < 0 && y < 0 && y < -13) ||
          (x >= 13 && x < 34 && y < 0 && y >= -21) ||
          (x >= 0 && x < 21 && y >= 13 && y < 34)
        ) {
          if (rand(21)) {
            game.bornCell({ x: x, y: y }); // Spawn cell
          }
        }
        // 13
        if (
          (x >= -13 && x < 0 && y >= 8 && y < 21) ||
          (x >= 8 && x < 21 && y >= 0 && y < 13) ||
          (x >= 0 && x < 13 && y < -8 && y >= -21) ||
          (x >= -21 && x < -8 && y < 0 && y >= -13)
        ) {
          if (rand(13)) {
            game.bornCell({ x: x, y: y }); // Spawn cell
          }
        }
        // 5
        if (
          (x >= -13 && x < -8 && y >= 0 && y < 5) ||
          (x >= 0 && x < 5 && y >= 8 && y < 13) ||
          (x >= 8 && x < 13 && y < 0 && y >= -5) ||
          (x >= -5 && x < 0 && y < -8 && y >= -13)
        ) {
          if (rand(5)) {
            game.bornCell({ x: x, y: y }); // Spawn cell
          }
        }
        // 3
        if (
          (x >= -13 && x < -10 && y >= 5 && y < 8) ||
          (x >= 5 && x < 8 && y >= 10 && y < 13) ||
          (x >= 10 && x < 13 && y < -5 && y >= -8) ||
          (x >= -8 && x < -5 && y < -10 && y >= -13)
        ) {
          if (rand(3)) {
            game.bornCell({ x: x, y: y }); // Spawn cell
          }
        }
        // 2
        if (
          (x >= -10 && x < -8 && y >= 6 && y < 8) ||
          (x >= 6 && x < 8 && y > 7 && y <= 9) ||
          (x >= 8 && x < 10 && y < -6 && y >= -8) ||
          (x >= -8 && x < -6 && y > -11 && y < -8)
        ) {
          if (rand(2)) {
            game.bornCell({ x: x, y: y }); // Spawn cell
          }
        }
        // 1
        if (
          (x >= -10 && x < -8 && y >= 5 && y < 6) ||
          (x >= 5 && x < 6 && y >= 8 && y < 10) ||
          (x >= 8 && x < 10 && y < -5 && y > -7) ||
          (x >= -6 && x < -5 && y < -8 && y > -11)
        ) {
          game.bornCell({ x: x, y: y }); // Spawn cell
        }
      });
      */

      //game.startEvolution();
    }
  }, [game]);

  return (
    <div className="App">
      <canvas ref={canvasRef} />
    </div>
  );
}

export default App;
