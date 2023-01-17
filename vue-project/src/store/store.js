import { createStore } from "vuex";

const store = createStore({
    state (){
        return{
            originImg:[],
            paintImg:[],
            answer:[],
            result:[],
            rank:'A',
        }
    },
    mutations:{
        setOrigin(state,img){
            state.originImg=img
        },
        setPaint(state,gif){
            state.paintImg=gif
        },
        setAnswer(state,answer){
            state.answer=answer
        },
        setResult(state,result){
            state.result=result
        },
        setRank(state,rank){
            state.rank=rank
        }
    }
});


export default store