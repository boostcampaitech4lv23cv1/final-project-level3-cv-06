import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

const store = createStore({
    /**
     * The state function for the global variant.
     * @returns {Object}
     * 
     * @property {Array<String>} originImg 원본 이미지 url 배열
     * @property {Array<String>} paintImg 게임 이미지(gif) url 배열
     * @property {Array<String>} answerList 게임 정답 배열
     * @property {Array<String>} imgPath 서버와 통신하기 위해 쓰이는 이미지 url 배열
     * @property {Array<Boolean>} correctList 각 문제에 대하여 정답 여부를 담은 배열
     * @property {Number} clearTime 게임 클리어하는데 걸린 시간(% 단위 100->0)
     * @property {Number} correctAnswer 유저가 맞춘 정답 개수
     * @property {String} category 유저가 선택한 카테고리 저장
     */
    state (){
        return{
            originImg:[],
            paintImg:[],
            answerList:[],
            imgPath:[],
            correctList:[],
            clearTime:100,
            correctAnswer:0,
            category:'',
        }
    },


    mutations:{
        /**
         * 원본 이미지 url을 저장하기 위한 함수
         * @function setOrigin
         * @param {State} state vuex 변수 객체
         * @param {Array<String>} 원본 이미지 url 배열
         */
        setOrigin(state,img){
            state.originImg=img
        },


        /**
         * 게임 gif url을 저장하기 위한 함수
         * @function setPaint
         * @param {State} state vuex 변수 객체
         * @param {Array<String>} paint gif 이미지 url 배열
         */
        setPaint(state,paint){
            state.paintImg=paint
        },


        /**
         * 게임 정답을 저장하기 위한 함수
         * @function setAnswer
         * @param {State} state vuex 변수 객체
         * @param {Array<String>} answer 정답 배열 
         */
        setAnswer(state,answer){
            state.answerList=answer
        },


        /**
         * 각 문제에 대한 정답 여부와 총 몇 문제를 맞췄는지 구하기 위한 함수
         * @function setCorrect
         * @param {State} state vuex 변수 객체
         * @param {Array<Boolean>} correct 정답 오답 여부 배열 
         */
        setCorrect(state,correct){
            state.correctList=correct
            state.correctAnswer=0
            for(let i=0; i<9; i++){
                if(correct[i]==true){
                    state.correctAnswer+=1
                }
            }
        },


        /**
         * 클리어 타임을 저장하기 위한 함수
         * @function setCleartime
         * @param {State} state vuex 변수 객체
         * @param {Number} clearTime 게임 클리어 시간 퍼센트 
         */
        setCleartime(state,cleartime){
            state.clearTime=cleartime
        },


        /**
         * 서버에 보내주기 위한 url 배열 저장 함수
         * @function setPath
         * @param {State} state vuex 변수 객체
         * @param {Array<String>} path url 배열 
         */
        setPath(state,path){
            state.imgPath=path
        },


        /**
         * 카테고리 저장을 위한 함수
         * @function setCategory
         * @param {State} state vuex 변수 객체
         * @param {String} category 카테고리 명
         */
        setCategory(state,category){
            state.category=category
        }
    },
    plugins : [ 
        createPersistedState({})
    ],
});


export default store