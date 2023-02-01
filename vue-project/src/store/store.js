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
            name:'',
            correctAnswer:0,
            mode:'',
            category:'',
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
        setCleartime(state,cleartime){
            state.clearTime=cleartime
        },
        setCorrectanswers(state,correctanswers){
            state.correctAnswers=correctanswers
            state.correctAnswer=0
            for(let i=0; i<9; i++){
                state.correctAnswer+=1
            }
        },
        setPath(state,path){
            state.imgPath=path
        },
        setName(state,name){
            state.name=name
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