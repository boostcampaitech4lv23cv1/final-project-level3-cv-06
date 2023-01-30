import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import { set, keys, getAll } from "../store/idb.js";

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
            translations:[],
            clearTime:null,
        }
    },
    mutations:{
        addTranslation(state, translation) {
            set(translation.id, translation.image)
        },
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
    actions: {
        async POPULATE_FROM_CACHE({ state }) {
            let [keyss, values] = await Promise.all([keys(), getAll()])
            state.translations = keyss.map((key, index) => ({ id: key, name: values[index] }))
        },

    },
    plugins : [ 
        createPersistedState({
            paths: ['originImg', 'paintImg', 'answerList', 'imgPath', 'rank', 'corrrectList', 'refresh']
        })
    ],
});


export default store