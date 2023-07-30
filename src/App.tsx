import "./App.css";

import { useEffect } from "react";
import { Point, useGameLife } from "react-game-life";

let prevAliveBoard: Point[] = [];
let prevDeadBoard: Point[] = [];

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
      board: { zoom: 30 /*2*/, height: 2000, width: 2000 },
      colors: { background: "#000", cell: "#00FF00" },
    },
    game: { onNextGeneration: oNextGeneration },
  });

  // calculate change in energy
  function oNextGeneration(board: Point[]) {
    // Alive Energy
    const aliveBoard = board;

    let prevAliveDistance = 0;
    prevAliveBoard.forEach((p) => {
      prevAliveDistance += Math.sqrt((0 - p.x) ** 2 + (0 - p.y) ** 2);
    });

    let aliveDistance = 0;
    aliveBoard.forEach((p) => {
      aliveDistance += Math.sqrt((0 - p.x) ** 2 + (0 - p.y) ** 2);
    });

    const aliveVelocity = aliveBoard.length - prevAliveBoard.length + 1;
    const aliveEnergy =
      (aliveDistance - prevAliveDistance + 1) * aliveVelocity ** 2;

    console.log("Alive Energy Change: " + aliveEnergy);

    // Dead Energy

    const allX = board.map((p) => p.x);
    const allY = board.map((p) => p.y);

    const minX = Math.min(...allX);
    const minY = Math.min(...allY);
    const maxX = Math.max(...allX);
    const maxY = Math.max(...allY);

    const p0 = [minX, maxY];
    const p2 = [maxX, minY];

    let deadBoard = [];

    if (isFinite(p0[0])) {
      for (let y = p0[1]; y >= p2[1]; y--) {
        for (let x = p0[0]; x <= p2[0]; x++) {
          if (!board.find((p) => p.x === x && p.y === y)) {
            deadBoard.push({ x: x, y: y });
          }
        }
      }
    }

    let prevDeadDistance = 0;
    prevDeadBoard.forEach((p) => {
      prevDeadDistance += Math.sqrt((0 - p.x) ** 2 + (0 - p.y) ** 2);
    });

    let deadDistance = 0;
    deadBoard.forEach((p) => {
      deadDistance += Math.sqrt((0 - p.x) ** 2 + (0 - p.y) ** 2);
    });

    const deadVelocity = deadBoard.length - prevDeadBoard.length + 1;
    const deadEnergy =
      (aliveDistance - prevAliveDistance + 1) * deadVelocity ** 2;

    console.log("Dead Energy Change: " + deadEnergy);

    prevAliveBoard = [...aliveBoard];
    prevDeadBoard = [...deadBoard];

    return {};
  }

  useEffect(() => {
    if (game) {
      document.addEventListener("click", (event) => {
        console.log(game.getCells());
      });

      //game.speedUp(20);

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
      /* loops each region area and adds cells */

      // TODO: alternate quadrant dead/alive?

      const width = 34;
      const phi = (Math.sqrt(5) + 1) / 2;
      const side = Math.round(width / 2);

      // a = 21, b = 13, c = 8 ....
      // outer arc corner, inner arc corner

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
          let x1, y1, x2, y2;

          if (q === 0 || q === 2) {
            x1 = Math.round(c[0][0]);
            y1 = Math.round(c[0][1]);
            x2 = Math.round(c[1][0]);
            y2 = Math.round(c[1][1]);
          } else {
            x1 = Math.round(c[0][1]);
            y1 = Math.round(c[0][0]);
            x2 = Math.round(c[1][1]);
            y2 = Math.round(c[1][0]);
          }

          const side = Math.abs(x1 - x2);

          const sX = x2 < x1 ? x2 : x1;
          const sY = y2 < y1 ? y2 : y1;

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

              if (Math.random() < fibPercent[i]) {
                game.bornCell({ x: nX, y: nY }); // Spawn cell
              }
            }
          }
        });
      });

      // Sierpinski triangle concept
      /*
      const midPoint = ([x1, y1]: any, [x2, y2]: any) => {
        return [Math.floor((x1 + x2) / 2), Math.floor((y1 + y2) / 2)];
      };

      const ST_Recur = (level: any, p1: any, p2: any, p3: any) => {
        if (level === 1) {
          const p = { x: p1[0], y: p1[1] };

          game?.bornCell({ x: p.x, y: p.y });
          game?.bornCell({ x: p.x + 1, y: p.y });
          game?.bornCell({ x: p.x, y: p.y + 1 });
          game?.bornCell({ x: p.x + 1, y: p.y + 1 });
        } else {
          const p4 = midPoint(p1, p2);
          const p5 = midPoint(p2, p3);
          const p6 = midPoint(p1, p3);

          ST_Recur(level - 1, p1, p4, p6);
          ST_Recur(level - 1, p4, p2, p5);
          ST_Recur(level - 1, p6, p5, p3);
        }
      };

      const T = [
        [0, 0],
        [149, 0],
        [0, 149],
      ];

      ST_Recur(6, T[0], T[1], T[2]);
      */

      /* logarithmic spiral decay probabilities
      const cells = 1156; // 34x34
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

      // game.startEvolution();
      */
    }
  }, [game]);

  return (
    <div className="App">
      <canvas ref={canvasRef} />
    </div>
  );
}

export default App;
