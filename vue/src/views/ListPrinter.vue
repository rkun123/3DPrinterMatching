<template>
    <div>

        
        

    </div>
</template>

<script>
    export default {

        data() {
            return {
                form_data: []
            }
        },
        
        async mounted () {



                    const requestOptions = {
                    method: "GET",
                        headers: { "Authorization": "Token " + this.$store.state.setUserKey },
                }


                fetch('http://127.0.0.1:8000/api/v1/printer3d/', requestOptions)
                    .then(response => response.json())
                    .then((data) => {
                      console.log(data);
                    });









            },
  


    }
</script>

<style scoped>
</style>
