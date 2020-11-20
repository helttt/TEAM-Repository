<template>
    <view class="content" >
		<image class="background" src="../../static/tabs/login.png">	
			
        <view class="title">
            <p>IMMEDIATE</p>
		</view>
		
		<view class="subtitle">
			<p>健 康 管 理</p>
		</view>
		
        <view>
            <p>账号</p>
            <input type="text" v-model="form.email" class="username">
<!--            <p>密码</p>
            <input type="password" v-model="form.password" class="username"> -->
        </view>
		
        <view>
            <button type="primary" class="login" @click="submit" >登录</button>
        </view>
    </view>
</template>

<script>
    // import {mapActions} from 'vuex'
    // export default {
    //     data() {
    //         return {
    //             form:{
    //                 email: '',
    //                 password: '',
    //             }
    //         }
    //     },
    //     onLoad() {

    //     },
    //     methods: {
    //         ...mapActions([
    //             'handleLogin',
    //             'getUserInfo'
    //         ]),
    //         submit(){
    //             this.handleLogin(this.form).then(() => {
    //                 this.getUserInfo().then(() => {
    //                     uni.showToast({
    //                         icon: 'success',
    //                         position: 'bottom',
    //                         title: '登录成功'
    //                     })
    //                     // uni.navigateBack()   小程序用这个  把首页路由放第一个
    //                     uni.navigateTo({
    //                         url: '../index/index'
    //                     });
    //                 })
    //             })
    //         }
    //     }
    // }
</script>

<style scoped>
	.background{
			position: fixed;
			width:100%;
			height:100%;
			top:0;
			left:0;
			z-index:-1;
	}
	
    .title{
        font-weight:300;
        margin: 150rpx 0 0 0;
        font-size: 100rpx;
        color: white;
    }
	
	.subtitle{
		font-weight: 200;
		margin:0 0 20rpx 0;
		font-size:40rpx;
		color:#999999;
	}
    .username{
        height: 120rpx;
        margin:50rpx 0 40rpx 0;
        width: 600rpx;
        border-radius: 40rpx;
        border: white 3rpx solid;
        background-color: rgba(188, 197, 204, 0.4);
    }
    .content {
        background-size: 100% 100%;
        padding: 70rpx;
        margin: 0 auto;
        text-align: center;
        height: 90.3vh;
    }
    .login{
		height: 120rpx;
		margin:80rpx 0 40rpx 0;
		width: 600rpx;
		border-radius: 40rpx;
		border: white 3rpx solid;
        background-color: rgba(188, 197, 204, 0.4);
    }
	
</style>
