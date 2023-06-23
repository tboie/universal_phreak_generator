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
        //console.log(game.getCells());
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

      /* 2 spiral merge base (opposite direction) */
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
                /* 2 spiral merge base
                game.bornCell({ x: ii * 8 + gX, y: i * 8 + gY });
                */
              }
            });
          });
        });
      });

      /* golden spiral regions */

      const width = 136;
      const phi = (Math.sqrt(5) + 1) / 2;
      const side = Math.round(width / 2);

      // a = 21, b = 13, c = 8 ....
      const aX = side / phi;
      const aY = side - aX;
      const aC = [
        [aX, side],
        [0, aY],
      ];

      const bY = aX / phi;
      const bC = [
        [aX, 0],
        [bY / phi, aY],
      ];

      const cY = bY / phi;
      const cC = [
        [0, 0],
        [cY, cY],
      ];

      const dC = [
        [0, aY],
        [cY / phi, cY],
      ];

      const eY = cY + (aY - cY) / phi / phi;
      const eC = [
        [cY, aY],
        [cY / phi, eY],
      ];

      const fX = (cY / phi) * 2;
      const fC = [
        [cY, cY],
        [fX / phi, eY],
      ];

      // TODO: smallest 2 squares

      const fibPercent = [21, 13, 8, 5, 3, 2].map((n) => 100 / n / 100);

      [0, 1, 2, 3].forEach((q) => {
        [aC, bC, cC, dC, eC, fC].forEach((c, i) => {
          let x1 = Math.round(c[0][0]);
          let y1 = Math.round(c[0][1]);
          let x2 = Math.round(c[1][0]);
          let y2 = Math.round(c[1][1]);

          /* rotate */
          if (q === 1 || q === 3) {
            x1 = Math.round(c[0][1]);
            y1 = Math.round(c[0][0]);
            x2 = Math.round(c[1][1]);
            y2 = Math.round(c[1][0]);
          }

          const side = Math.abs(x1 - x2);

          let sX = x2 < x1 ? x2 : x1;
          let sY = y2 < y1 ? y2 : y1;

          for (let x = sX; x < sX + side; x++) {
            for (let y = sY; y < sY + side; y++) {
              let nX = x;
              let nY = y;

              if (q === 0 || q === 1) {
                nY *= -1;
                nY -= 1;
              }
              if (q === 0 || q === 3) {
                nX *= -1;
                nX -= 1;
              }

              const r = Math.random();
              if (r < fibPercent[i]) {
                game.bornCell({ x: nX, y: nY }); // Spawn cell
              }
            }
          }
        });
      });

      /* logarithmic spiral decay probabilities
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

        // logarithmic spiral decay algorithm
        const prob = (100 - (100 / cells) * i) / 100;
        const d = Math.random();

        if (d < prob) {
          game.bornCell({ x: p[0], y: p[1] }); // Spawn cell
        }
      });
      */

      // game.startEvolution();
    }
  }, [game]);

  return (
    <div className="App">
      <canvas ref={canvasRef} />
    </div>
  );
}

export default App;
