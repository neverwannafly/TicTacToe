let fitness = function(state, goal_state) {
    let score = 0;
    for (let i=0; i<state.length; i++) {
    	for (let j=0; j<state[0].length; j++) {
            score += state[i][j]!=goal_state[i][j];
        }
    }
    return score;
}

// Queue
let _capacity = 100000005;
let _size = 0;
let Q = new Array(_capacity);

let Node = function(key,state) {
    this.key = key;
    this.state = state;
}
function reset() {
    _size = 0;
    Q = new Array(_capacity);
}
function add(el) {
    Q[_size] = el;
    let idx = _size;
    let parent = _parent(idx);
    while (parent>=0 && Q[parent].key > Q[idx].key) {
        _swap(parent, idx);
        idx = parent;
        parent = _parent(idx);
    }
    if (_capacity != _size)
        _size++;
}
function front() {
    return Q[0];
}
function remove() {
    if (_size==0) throw new Error("Underflow!");
    _swap(0, --_size);
    _heapify(0);
}
function empty() {
    return _size == 0;
}
function _parent(idx) {
    return Math.floor((idx-1)/2);
}
function _swap(idx1, idx2) {
    let tmp = Q[idx1];
    Q[idx1] = Q[idx2];
    Q[idx2] = tmp;
}
function _heapify(idx) {
    let left = 2*idx+1;
    let right = 2*idx+2;
    let min = idx;
    if (left<_size && Q[left].key<Q[min].key) {
        min = left;
    }
    if (right<_size && Q[right].key<Q[min].key) {
        min = right;
    }
    if (idx != min) {
        _swap(idx, min);
        _heapify(min);
    }
}

let Astar = function(start_state, goal_state) {
    let visited = {};
    reset();
    add(new Node(0, start_state));
    while (!empty()) {
        let u = front(); remove();
        if (u.state.toString() == goal_state.toString()) {
            return true;
        }
        if (u.state in visited) {
            continue;
        }
        console.log(u.state);
        visited[u.state.toString()] = true;
        let i=0, j=0;
        while (i<goal_state.length) {
            j = 0;
            while (j<goal_state[0].length) {
                if (u.state[i][j]==0) break;
                j++;
            }
            if (u.state[i][j]==0) break;
            i++;
        }
        if (i+1 < goal_state.length) {
            let new_state = JSON.parse(JSON.stringify(u.state));
            let tmp = new_state[i+1][j];
            new_state[i+1][j] = new_state[i][j];
            new_state[i][j] = tmp;
            add(new Node(fitness(new_state, goal_state), new_state));
        }
        if (i-1 >= 0) {
            let new_state = JSON.parse(JSON.stringify(u.state));
            let tmp = new_state[i-1][j];
            new_state[i-1][j] = new_state[i][j];
            new_state[i][j] = tmp;
            add(new Node(fitness(new_state, goal_state), new_state));
        }
        if (j+1 < goal_state.length) {
            let new_state = JSON.parse(JSON.stringify(u.state));
            let tmp = new_state[i][j+1];
            new_state[i][j+1] = new_state[i][j];
            new_state[i][j] = tmp;
            add(new Node(fitness(new_state, goal_state), new_state));
        }
        if (j-1 >= 0) {
            let new_state = JSON.parse(JSON.stringify(u.state));
            let tmp = new_state[i][j-1];
            new_state[i][j-1] = new_state[i][j];
            new_state[i][j] = tmp;
            add(new Node(fitness(new_state, goal_state), new_state));
        }
    }
    return false;
}

let ss = [[1,2,5],[4,3,8],[7,0,6]];
let gs = [[1,2,3],[4,5,6],[7,8,0]];

console.log(Astar(ss, gs));
