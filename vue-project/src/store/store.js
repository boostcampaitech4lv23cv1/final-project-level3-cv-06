import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

const store = createStore({
    state (){
        return{
            originImg:[],
            paintImg:[],
            answerList:[],
            imgPath:[],
            rank:'S',
            corrrectList:[],
        }
    },
    mutations:{
        setOrigin(state,img){
            state.originImg=img
            state.imgPath=img
        },
        setPaint(state,gif){
            state.paintImg=gif
        },
        setAnswer(state,answer){
            state.answerList=answer
        },
        setRank(state,rank){
            state.rank=rank
        },
        setCorrect(state,correct){
            state.corrrectList=correct
        }

    },
    plugins : [ createPersistedState() ],
});


export default store