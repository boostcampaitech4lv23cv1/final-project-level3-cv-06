import axios from 'axios';
export default{
    methods:{
        /**
         * 서버와 json 형식으로 통신하기 위한 함수
         * @function $api
         * @param {String} url 통신할 서버의 url
         * @param {String} method GET,POST등 통신 방식
         * @param {Tuple} data 서버에 보낼 데이터
         */
        async $api(url,method,data={}){
            return (await axios({
                method: method,
                url,
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data),
            }).catch(e=>{
                console.log(e);
            })
            ).data;
        },


        /**
         * 서버와 form 데이터 형식으로 통신하기 위한 함수
         * @function $api2
         * @param {String} url 통신할 서버의 url
         * @param {String} method GET,POST등 통신 방식
         * @param {formData} data 서버에 보낼 데이터
         */
        async $api2(url,method,data){
            return (await axios({
                method: method,
                url,
                headers: {
                    'Content-Type': 'multipart/form-data'
                  },
                data
            }).catch(e=>{
                console.log(e);
            })
            ).data;
        }
    }
}
