import axios from 'axios';
export default{
    methods:{
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
