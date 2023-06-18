import "./App.css";

import { useEffect } from "react";
import { Point, useGameLife } from "react-game-life";

// import megaPiece1 from "./megaPiece1";
// import megaPattern1 from "./megaPattern";
// import megaPiecMorph2 from "./megaPieceMorph2";
// import megaPieceMorph6 from "./megaPieceMorph6";

let prevBoard: Point[] = [];
let prevDistance = 0;

/*** ***/
// Glider Templates
/** ***/

const g0 = [
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
];

const g1 = [
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
];

const g2 = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
];

const g3 = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
];

// nothing
const r0 = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
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
      board: { zoom: 15 /*2*/ },
      colors: { background: "#000", cell: "#00FF00" },
    },
    game: { onNextGeneration: oNextGeneration },
  });

  // calculate change in energy
  function oNextGeneration(board: Point[]) {
    let energy = 0;
    let distance = 0;
    let velocity = board.length - prevBoard.length + 1;

    if (board.length > 1) {
      // TODO: use center point
      const p1 = board[1];

      board.forEach((p2, i) => {
        if (i > 0) {
          distance += Math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2);
        }
      });
    }

    energy = (distance - prevDistance + 1) * velocity ** 2;
    console.log(energy);

    prevBoard = [...board];
    prevDistance = distance;

    return {};
  }

  useEffect(() => {
    if (game) {
      document.addEventListener("click", (event) => {
        console.log(game.getCells());
      });

      game.speedUp(20);

      /*
      megaPattern1.forEach((p) => {
        game.bornCell({ x: p.x, y: p.y });
      });

      megaPieceMorph6.forEach((p) => {
        game.bornCell({ x: p.x, y: p.y });
      });

      /* random 4 gliders
      const gliders = [
        [rG(), rG()],
        [rG(), rG()],
      ];
      */

      /* model to create mega pattern
      const gliders = [
        [
          [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
          ],
          [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
          ],
        ],
        [
          [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
          ],
          [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
          ],
        ],
      ];
      */

      /* largest mega 8 piece mega pattern
      const gliders = [
        [r0, r0, r0, r0, g0, g3, r0, r0],
        [r0, r0, r0, r0, g3, g0, r0, r0],
        [r0, r0, r0, r0, r0, r0, r0, r0],
        [r0, r0, r0, r0, r0, r0, r0, r0],
        [r0, r0, r0, r0, r0, r0, r0, r0],
        [r0, r0, r0, r0, r0, r0, r0, r0],
        [r0, r0, r0, r0, r0, r0, r0, r0],
        [r0, r0, r0, r0, r0, r0, r0, r0],
        [r0, r0, r0, r0, g2, g1, r0, r0],
        [r0, r0, r0, r0, g1, g2, r0, r0],
      ];

      */

      /* WIP
      const gliders = [
        [g0, g3, r0, r0, r0, r0, r0, r0, r0, r0, r0],
        [g3, g0, r0, r0, r0, r0, r0, r0, r0, r0, r0],

        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],

        [g2, g1, r0, r0, r0, r0, r0, r0, r0, r0, r0],
        [g1, g2, r0, r0, r0, r0, r0, r0, r0, r0, r0],

        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],

        [g0, g3, r0, r0, r0, r0, r0, r0, r0, r0, r0],
        [g3, g0, r0, r0, r0, r0, r0, r0, r0, r0, r0],

        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],

        [g2, g1, r0, r0, r0, r0, r0, r0, r0, r0, r0],
        [g1, g2, r0, r0, r0, r0, r0, r0, r0, r0, r0],
      ];
      */

      /* largest 16 piece mega pattern
      const gliders = [
        [g0, g3, r0, r0, r0, r0, r0, r0, r0, r0, r0],
        [g3, g0, r0, r0, r0, r0, r0, r0, r0, r0, r0],

        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],

        [g2, g1, r0, r0, r0, r0, r0, r0, r0, r0, r0],
        [g1, g2, r0, r0, r0, r0, r0, r0, r0, r0, r0],

        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],

        [g0, g3, r0, r0, r0, r0, r0, r0, r0, r0, r0],
        [g3, g0, r0, r0, r0, r0, r0, r0, r0, r0, r0],

        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],

        [g2, g1, r0, r0, r0, r0, r0, r0, r0, r0, r0],
        [g1, g2, r0, r0, r0, r0, r0, r0, r0, r0, r0],
      ];
      */

      /* largest 32 piece mega pattern
      const gliders = [
        [g0, g3, r0, r0, r0, r0, r0, r0, r0, r0, r0, g0, g3],
        [g3, g0, r0, r0, r0, r0, r0, r0, r0, r0, r0, g3, g0],

        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],

        [g2, g1, r0, r0, r0, r0, r0, r0, r0, r0, r0, g2, g1],
        [g1, g2, r0, r0, r0, r0, r0, r0, r0, r0, r0, g1, g2],

        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],

        [g0, g3, r0, r0, r0, r0, r0, r0, r0, r0, r0, g0, g3],
        [g3, g0, r0, r0, r0, r0, r0, r0, r0, r0, r0, g3, g0],

        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],
        [r0, r0],

        [g2, g1, r0, r0, r0, r0, r0, r0, r0, r0, r0, g2, g1],
        [g1, g2, r0, r0, r0, r0, r0, r0, r0, r0, r0, g1, g2],
      ];
      */

      /* console.log(gliders); */
      const gliders = [[rG()]];

      gliders.forEach((gs, i) => {
        gs.forEach((g, ii) => {
          g.forEach((gRow, gX) => {
            gRow.forEach((gCell, gY) => {
              if (gCell) {
                // +x for padding
                game.bornCell({ x: ii * 4 + gX, y: i * 4 + gY });
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
