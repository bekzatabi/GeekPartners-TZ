<template>
  <div class="orders">
      <div class="orders__container">
        <div class="orders__title">
            Список заказов
        </div>
        <my-button @click="createOrder" class="orders__create_btn">
            Создать заказ 
        </my-button>
      </div>
        <my-dialog @hideFunc="hideDialogQWE" v-model:show="dialogVisible">
            <post-form 
                @statusUpdated="getOrders"
                :order="current_order"
             />
        </my-dialog>
        <order-item
            v-for="order in orders_data"
            :key="order.number"
            :order="order"
            @remove="removeOrder"
            @openDialog="showDialog"
            @deleteProduct="deleteProduct"
        />
    
  </div>
</template>

<script>
import OrderItem from '../components/OrderItem.vue';
import PostForm from '../components/PostForm.vue';
import MyButton from '../components/UI/MyButton.vue';
import axios from '../config/axios';
export default {
  components: { MyButton, PostForm, OrderItem },
    data(){
        return {
            orders_data: [],
            current_order: {},
            dialogVisible: false,
        }
    },
    methods:{
         createOrder(){
            axios.post('/orders').then(res=>{
               this.orders_data.push(res.data)
            })
        },
        hideDialogQWE(bool){
            this.dialogVisible = bool;
        },
         showDialog(order){
             console.log(order)
            this.dialogVisible = true;
            this.current_order = order
        },
        removeOrder(order){
            console.log(order.id)
            axios.delete(`/orders`,{
                params:{ id: order.id}
            }).then(res=>{
                this.orders_data = res.data
            })
        },
        getOrders(){
            axios.get('/orders').then(res=>{
                        this.orders_data = res.data
                        console.log(this.orders_data)
                        console.log(res.data)
            })
        },
        deleteProduct(){
            this.getOrders()
        }
    },
    mounted(){
       this.getOrders()
    }
}
</script>

<style scoped>
    .orders{
        font-size: 30px;
        color: teal;
    }
    .orders__container{

    }
    .orders__title{

    }
    .orders__create_btn{
        background-color:teal;
        color: #fff;
        cursor: pointer;
    }
    .orders__create_btn:hover{
        opacity: .6;
    }
</style>