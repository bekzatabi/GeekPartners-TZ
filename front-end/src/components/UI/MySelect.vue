<template>
    <select v-model="modelValue" @change="changeOption">
        <option disabled value="">Выберите из списка</option>
        <option 
        v-for="option in options" 
        :key="option.value" 
        :value="option.id"
        >
            {{ option.name }}
        </option>
    </select>
  
</template>

<script>
export default {    
    name: 'my-select',
    props:{
        isCreated:{
            type: Boolean,
            default: false,
        },
        modelValue:{
            type: String
        },
        options:{
            type: Array,
            default: () => []
        }
    },
    methods: {
        changeOption(event){
            this.$emit('changed', event.target.value);
        },
    }

}
</script>

<style scoped>
    select{
        margin-top: 20px;
        height:30px
    }
</style>