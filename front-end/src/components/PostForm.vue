<template>
  <form @submit.prevent>
            <h4>Добавить товар к заказу</h4>
            <my-input 
                v-model="post.product_name"
                type="text" 
                placeholder="Название"
            />
            <my-input 
                v-model="post.product_count"
                type="number" 
                placeholder="Кол-во"
            />
            <my-select
                @changed="changeOp"
                :options="status_list"
            />
            <my-button 
                style="align-self: flex-end; margin-top: 15px;cursor:pointer"
                @click="setProduct"
            >
            ОК
            </my-button>
        </form>
</template>

<script>
import MySelect from './UI/MySelect.vue';
import axios from '../config/axios';
export default {
  components: { MySelect },
    props:{
        order: {
            type: Object,
            required: false,
        }
    },
    data() {
        return{
            current_status: "",
            status_list: [
                {value: 'created', name: 'Создано'},
                {value: 'in_process', name: 'В процессе'},
                {value: 'success', name: 'Выполнено'},
            ],
            post: {
                product_name: '',
                product_count: '',
                product_status: ''
            }
        }
    },
    methods: {
        changeOp(id){
            this.current_status = id
        },
        setProduct(){
            console.log(this.current_status)
            if(this.post.product_name && this.post.product_count){
                  axios.post('/add_product',{
                order: this.order.id,
                product: this.post.product_name,
                amount: this.post.product_count
            }).then(res=>{
                console.log(res.data)
            })
            }

            axios.put('/orders',{
                status: this.current_status
            },{
                params:{
                    id: this.order.id,
                }
            }).then(res=>{
                this.$emit("statusUpdated")
            })
        }
    },
    mounted(){
        axios.get('/status').then(res=>console.log(this.status_list = res.data.result))
    }
}
</script>

<style>
form{
    display: flex;
    flex-direction: column;
}


</style>