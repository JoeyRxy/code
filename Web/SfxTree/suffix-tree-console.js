const defaultIfZero = (a, x) => x === 0 ? a : x;
const isDefined = x => x !== void 0;
const isUndefined = x => x === void 0;

const NONE = Symbol('NONE');

const chalk = require('chalk');
const val = x => (x === NONE ? (x = 'none', chalk.bold.grey) : chalk.cyan)(String(x));
let highlightActiveNode = null;
let highlightedEdges = [];
let highlightLinkFrom = null, highlightLinkTo = null;
let nextId = 0;

function newSuffixTree (array) {
  const root = { id: 0, edges: new Map(), link: null };
  const tree = { array, root };

  if (array.length <= 0) {
    return tree;
  }

  let activeNode = root;
  let activeEdge = NONE;
  let activeLength = 0;
  let remainder = 0;
  let currentIndex = 0;
  let elementAtCurrentPosition = array[0];
  let edge, latestAddedNode;

  let halt = false;
  let previousIndex = -1;
  let substep = 1;

  let count = 0;
  do {
    if (++count > 100) throw new Error('Infinite loop');

    const lengthToRender = currentIndex + 1;

    if (currentIndex !== previousIndex) {
      previousIndex = currentIndex;
      substep = 1;
      console.log(chalk.bold.grey('----------------------------------------------------------------------------\n'));
      const colouredString
        = (currentIndex === 0 ? '' : chalk.black.bgWhite(' ' + array.slice(0, currentIndex).join('') + ' '))
        + chalk.bgGreen.black(' ' + array[currentIndex] + ' ')
        + (currentIndex === array.length - 1 ? '' : chalk.black.bgWhite(' ' + array.slice(currentIndex + 1).join('') + ' '));
      console.log(`${chalk.bold.green(`Step #${currentIndex + 1}`)} [${val(currentIndex)}] ${colouredString}`);
    }
    else {
      console.log(chalk.green(`/ Iteration #${++substep}\n`));
    }

    if (count > 0) {
      highlightActiveNode = activeNode;
      console.log();
      console.log(renderTree(array.slice(0, lengthToRender), root));
    }

    console.log(`activeEdge: ${val(activeEdge)}, activeLength: ${val(activeLength)}, remainder: ${val(remainder)}`);
    console.log(!edge ? 'edge is undefined' : `edgeStart: ${val(edge && edge[0])}, edgeEnd: ${val(edge && edge[1])}`);
    console.log(chalk.magenta(array.slice(currentIndex - activeLength, currentIndex + 1).join('')));

    if (remainder === 0) {
      remainder = 1;
      activeLength = 0;
      activeEdge = array[currentIndex];
      console.log(`activeEdge is now: ${val(activeEdge)}`);
      edge = activeNode.edges.get(activeEdge);
    }
    else if (isUndefined(edge)) {
      console.log(activeNode.id, activeEdge);
      edge = activeNode.edges.get(activeEdge);
    }

    console.log(`edge is ${val(edge && JSON.stringify(edge))}`);

    if (isUndefined(edge)) {
      console.log('no edge at active node, inserting...');
      const newEdge = [currentIndex + activeLength, 0, null];
      highlightedEdges.push(newEdge);
      activeNode.edges.set(activeEdge, newEdge);
      remainder--;
      latestAddedNode = null;
      if (activeLength > 0) {
        console.log('decrementing activeLength');
        activeLength--;
      }
      if (activeNode !== root) {
        activeNode = activeNode.link === null ? root : activeNode.link;
      }
      else {
        currentIndex++;
      }
      edge = void 0;
    }
    else {
      let edgeLength;
      while (edge[1] !== 0 && (edgeLength = edge[1] - edge[0]) <= activeLength) {
        console.log(`active edge (length ${edgeLength}) was at index ${val(edge[1] - 1)}: ${chalk.magenta(activeEdge)}`);
        activeLength -= edgeLength;
        activeEdge = array[currentIndex - activeLength];
        activeNode = edge[2];
        console.log(`switched active node to ${activeNode.id}`);
        console.log(`active edge changed to index ${val(edge[1])}: ${chalk.magenta(activeEdge)}`, edge);
        highlightedEdges.push(edge);
        edge = activeNode.edges.get(activeEdge);
        if (isUndefined(edge)) {
          break;
        }
      }

      if (isDefined(edge)) {
        highlightedEdges.push(edge);
        const edgeIndex = edge[0] + activeLength;
        console.log(`edgeIndex: ${val(edgeIndex)}, currentIndex: ${val(currentIndex)}`);
        if (array[currentIndex] === array[edgeIndex]) {
          currentIndex++;
          remainder++;
          activeLength++;
          latestAddedNode = null;
          console.log(activeLength);
          if (edge[1] > 0) {
            const edgeLength = edge[1] - edge[0];
            if (edgeLength <= activeLength) {
              console.log('BROKEN');
              activeNode = edge[2];
              activeEdge = array[currentIndex];
              activeLength -= edgeLength;
              edge = void 0;
            }
          }
        }
        else {
          const tailEdge = [edgeIndex, edge[1], edge[2]];
          const newEdge = [currentIndex, 0, null];
          highlightedEdges.push(newEdge);
          const nextNode = {
            id: ++nextId,
            edges: new Map([
              [array[edgeIndex], tailEdge],
              [array[currentIndex], newEdge]
            ]),
            link: null
          };
          edge[1] = edgeIndex;
          edge[2] = nextNode;
          if (latestAddedNode !== null) {
            console.log(`suffix link created`);
            highlightLinkFrom = latestAddedNode;
            highlightLinkTo = nextNode;
            latestAddedNode.link = nextNode;
          }
          latestAddedNode = nextNode;

          console.log(`split at ${tailEdge[0]}`, elementAtCurrentPosition, newEdge);
          remainder--;
          if (activeNode === root) {
            activeLength--;
            activeEdge = array[currentIndex - activeLength];
            console.log(`setting edge to nothing (${activeEdge})`, currentIndex - activeLength, array[currentIndex - activeLength], edge[0], array[edge[0]], edge[1], array[edge[1]]);
            edge = void 0;
          }
          else {
            console.log(activeNode.link ? `following suffix link to node ${activeNode.link.id}` : 'no suffix link, resetting to root');
            activeNode = activeNode.link === null ? root : activeNode.link;
            // activeLength--;
            edge = void 0;
          }
        }
      }
    }
    highlightActiveNode = activeNode;

    console.log();
    console.log(renderTree(array.slice(0, lengthToRender), root));

    highlightedEdges.length = 0;
    highlightLinkFrom = null, highlightLinkTo = null;

    console.log(`currentIndex: ${currentIndex}, activeEdge: ${val(activeEdge)}, activeLength: ${val(activeLength)}, remainder: ${val(remainder)}\n`);

  } while (currentIndex < array.length && !halt);
}

// ---------------------------------------------------------------------------------------------------------------------

const stringOf = (length, char) => new Array(length + 1).join(char);
const drawLine = (c, edge) => highlightedEdges.includes(edge) ? chalk.bold.red(c) : chalk.grey(c);

function renderEdge (array, edge, prefix, maxEdgeLength) {
  const strEdge = array.slice(edge.startIndex, edge.endIndex || array.length).join('');
  let text = highlightedEdges.includes(edge.edge) ? chalk.bold.red(strEdge) : strEdge;
  if (edge.tail) {
    const line = stringOf(maxEdgeLength - strEdge.length + 1, '─');
    text += drawLine(line, edge.edge);
    text += renderTree(array, edge.tail, prefix + stringOf(strEdge.length + line.length, ' '));
  }
  else {
    text += '\n';
  }
  return text;
}

function renderTree (array, node, prefix = '') {
  let text = '';
  const strNum = String(node.id).padStart(2, '0');
  const strNode = node === highlightLinkTo ? `:${strNum}:` : `(${strNum})`;
  text += (node === highlightActiveNode ? chalk.bold.blue
    : node === highlightLinkFrom ? chalk.bold.cyan
    : node === highlightLinkTo ? chalk.bold.red
    : chalk.bold.grey)(strNode);
  if (node.edges.size === 0) return text;

  const endIndex = array.length;
  const edges = Array.from(node.edges)
    .map(([, e]) => ({ startIndex: e[0], endIndex: e[1] || endIndex, tail: e[2], edge: e }))
    .sort((a, b) => a.startIndex - b.startIndex + 1);
  const prefixWithNodePadding = prefix + stringOf(strNode.length, ' ');
  const maxEdgeLength = edges.reduce((n, edge) => Math.max(n, defaultIfZero(array.length, edge.endIndex) - edge.startIndex + 1), 0);

  for (let i = 0; i < edges.length; i++) {
    let connector, extender = ' ';

    if (i === 0) {
      if (edges.length > 1) {
        connector = drawLine('┬');
        extender = drawLine('│');
      }
      else {
        connector = drawLine('─', edges[i].edge);
      }
    }
    else {
      text += prefixWithNodePadding;
      if (i === edges.length - 1) {
        connector = drawLine('└');
      }
      else {
        connector = drawLine('├');
        extender = drawLine('│');
      }
    }

    text += connector + drawLine('─');
    const newPrefix = prefixWithNodePadding + extender + ' ';
    text += renderEdge(array, edges[i], newPrefix, maxEdgeLength);
  }

  return text;
}

const test = array => {
  console.log('\nCASE:', array.join(''), `(length: ${array.length})\n`);
  newSuffixTree(array);
};

// test(['A', 'B', 'C', 'A', 'B', 'X', 'A', 'B', 'C', 'D']);
// test('abcabxabcd'.split(''));
// test('almasamolmaz'.split(''));
// test('almasamo'.split(''));
// test('ooooooooo'.split(''));
// test('abcadak'.split(''));
// test('dedododeeodo'.split(''));
// test('abcdefabxybcdmnabcdex'.split(''));
test('mississippi'.split(''));