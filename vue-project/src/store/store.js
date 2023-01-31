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
            correctList:[],
            refresh:false,
            clearTime:100,
        }
    },
    mutations:{
        setOrigin(state,img){
            state.originImg=img
            // state.imgPath=img
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
            state.correctList=correct
        },
        setRefresh(state,refresh){
            state.refresh=refresh
        },
        setCleartime(state,cleartime){
            state.clearTime=cleartime
        },
        setCorrectanswers(state,correctanswers){
            state.correctAnswers=correctanswers
        },
        setPath(state,path){
            state.imgPath=path
        }

    },
    plugins : [ 
        createPersistedState({})
    ],
});


export default store