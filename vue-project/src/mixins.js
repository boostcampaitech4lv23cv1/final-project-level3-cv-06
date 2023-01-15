import axios from 'axios';
export default{
    methods:{
        async $api(url,method,data){
            return (await axios({
                method: method,
                url,
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data)
            }).catch(e=>{
                if(e.response.status === 422){
                    console.error(e.response.data);
                  }else{
                    console.error(e);
                  }
            })).data;
        }
    }
}
