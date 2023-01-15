import { createStore } from "vuex";

const store = createStore({
    state (){
        return{
            originImg:[],
            paintImg:[],
            answer:[],
            result:[],
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
    }
});


export default store