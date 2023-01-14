import { createStore } from "vuex";

const store = createStore({
    state (){
        return{
            origin_img:[],
            paint_img:[],
            answer:[],
        }
    },
    mutations:{
        get_origin(state,img){
            state.origin_img=img
        },
        get_paint(state,gif){
            state.paint_img=gif
        },
        get_answer(state,answer){
            state.answer=answer
        }
    }
});


export default store