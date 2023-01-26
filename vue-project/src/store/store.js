import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

const store = createStore({
    state (){
        return{
            originImg:[],
            paintImg:[],
            answer:[],
            result:[],
            rank:'S',
            imgList:[],
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
        },
        setPath(state,path){
            state.imgList=path
        }
    },
    plugins : [ createPersistedState() ],
});


export default store