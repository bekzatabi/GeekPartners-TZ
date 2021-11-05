<template>
    <div class="post">
        <div>
            <div><strong>Номер заказа: </strong>{{ order.number }}</div>
            <div v-show="order.data_order" v-for="product in order.data_order" :key="product.id" class="product">
                <div><strong>Название товара: </strong>{{ product.product }}</div>
                <div><strong>Кол-во: </strong>{{product.amount}}</div>   
                <button @click="deleteProduct(product.id)">delete</button>
            </div>
            <div><strong>Статус: </strong>{{order?.status?.name}}</div> 
             <div><strong>Дата: </strong>{{ order.created_at.substring(0,10) }}</div>     
        </div>
        <div class="post__btns">
            <my-button
                @click="this.$router.push(`/orders/${order.id}`)"
                >
                Открыть
            </my-button>
            <my-button
                @click="$emit('openDialog', order)"
                >
                Изменить
            </my-button>
            <my-button
                @click="$emit('remove', order)"
                >
                Удалить
            </my-button>
        </div>
        
    </div>
</template>

<script>
import axios from '../config/axios'
export default {
    props:{
        order: {
            type: Object,
            required: true,
        }
    },
    methods: {
        deleteProduct(id){

            axios.delete('/add_product',{
                params:{
                    id
                }
            }).then(res=>{
                this.$emit("deleteProduct")
            })
        }
    }
}
</script>

<style scoped>
.post{
    padding: 15px;
    border: 2px solid gray;
    margin-top: 15px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.product{
    margin-top: 10px;
    border: 1px solid red;
}
</style>