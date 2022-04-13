function solution(s) {
    let answer = '';
    let word = '';
    for ( const a of s){
        if(!Number(a) && a !== '0'){
            word += a
        }else{
            answer += a
        }
        if(graph[word]){
            answer += graph[word]
            word = ''
        }
    }
    return Number(answer);
}
const graph = {
    zero : "0",
    one : "1",
    two : "2",
    three : "3" ,
    four : "4",
    five : "5",
    six : "6",
    seven :"7" ,
    eight : "8",
    nine : "9"
}