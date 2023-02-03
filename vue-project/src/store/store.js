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
            clearTime:100,
            correctAnswer:0,
            mode:'',
            category:'',
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
            state.answerList=answer
        },
        setRank(state,rank){
            state.rank=rank
        },
        setCorrect(state,correct){
            state.correctList=correct
            state.correctAnswer=0
            for(let i=0; i<9; i++){
                if(correct[i]==true){
                    state.correctAnswer+=1
                }
            }
        },
        setCleartime(state,cleartime){
            state.clearTime=cleartime
        },
        setCorrectanswers(state,correctanswers){
        },
        setPath(state,path){
            state.imgPath=path
        },
        setMode(state,mode){
            state.mode=mode
        },
        setCategory(state,category){
            state.category=category
        }

    },
    plugins : [ 
        createPersistedState({})
    ],
});


export default store