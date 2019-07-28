const isDefined = x => x !== void 0;
const isUndefined = x => x === void 0;

const NONE = Symbol('NONE');

function newSuffixTree (array) {
  const root = { edges: new Map(), link: null };
  const tree = { array, root };

  if (array.length <= 0) {
    return tree;
  }

  let activeNode = root;
  let activeEdge = NONE;
  let activeLength = 0;
  let remainder = 0;
  let currentIndex = 0;
  let edge, latestAddedNode;

  do {
    if (remainder === 0) {
      remainder = 1;
      activeLength = 0;
      activeEdge = array[currentIndex];
      edge = activeNode.edges.get(activeEdge);
    }
    else if (isUndefined(edge)) {
      edge = activeNode.edges.get(activeEdge);
    }

    if (isUndefined(edge)) {
      const newEdge = [currentIndex + activeLength, 0, null];
      activeNode.edges.set(activeEdge, newEdge);
      remainder--;
      latestAddedNode = null;
      if (activeLength > 0) {
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
        activeLength -= edgeLength;
        activeEdge = array[currentIndex - activeLength];
        activeNode = edge[2];
        edge = activeNode.edges.get(activeEdge);
        if (isUndefined(edge)) {
          break;
        }
      }

      if (isDefined(edge)) {
        const edgeIndex = edge[0] + activeLength;
        if (array[currentIndex] === array[edgeIndex]) {
          currentIndex++;
          remainder++;
          activeLength++;
          latestAddedNode = null;
          
          if (edge[1] > 0) {
            const edgeLength = edge[1] - edge[0];
            if (edgeLength <= activeLength) {
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
          const nextNode = {
            edges: new Map([
              [array[edgeIndex], tailEdge],
              [array[currentIndex], newEdge]
            ]),
            link: null
          };
          edge[1] = edgeIndex;
          edge[2] = nextNode;
          
          if (latestAddedNode !== null) {
            latestAddedNode.link = nextNode;
          }
          latestAddedNode = nextNode;

          remainder--;
          
          if (activeNode === root) {
            activeLength--;
            activeEdge = array[currentIndex - activeLength];
            edge = void 0;
          }
          else {
            activeNode = activeNode.link === null ? root : activeNode.link;
            edge = void 0;
          }
        }
      }
    }
  } while (currentIndex < array.length);
}
