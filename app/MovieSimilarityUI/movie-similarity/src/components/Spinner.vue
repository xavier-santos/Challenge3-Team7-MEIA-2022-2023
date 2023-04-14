<template>
    <div class="spinner">
    <div class="spinner__background">
        <div class="spinner__circles">
            <div></div>
            <div></div>
        </div>
    </div>
    </div>
</template>

<style scoped>
  .spinner {
      bottom: 0px;
      left: 0px;
      display: flex;
      position: absolute;
      right: 0px;
      top: 0px;
      align-items: center;
      justify-content:  center;
      overflow: hidden;
      z-index: 999;
    }
    .spinner__background {
      bottom: 0px;
      left: 0px;
      position: absolute;
      right: 0px;
      top: 0px;
      background-color: rgba(255, 255, 255, 0.75)
    }
    .spinner__circles {
      position: absolute;
      top: 50%;
      left: 50%;
      display: block;
      transform: translate(-50%, -50%);
      width: 72px;
      height: 48px;
    }
    .spinner__circles div {
      position: absolute;
      top: 50%;
      display: block;
      width: 32px;
      height: 32px;
      box-sizing: border-box;
      transform: translate(0, -50%);
      border-radius: 50%;
      border: 2px solid #193f6e;
      background: white;
    }
    .spinner__circles div:nth-child(1) {
      left: 0;
      animation: circle-1 infinite;
      animation-timing-function: linear;
      animation-duration: 1s;
    }
    .spinner__circles div:nth-child(2) {
      right: 0;
      animation: circle-2 infinite;
      animation-timing-function: linear;
      animation-duration: 1s;
    }
    @keyframes circle-1 {
      0% {
        left: 0;
      }
      100% {
        left: calc(100% - 32px);
      }
    }
    @keyframes circle-2 {
      0% {
        right: 0;
        width: 32px;
        height: 32px;
      }
      50% {
        width: 48px;
        height: 48px;
      }
      100% {
        right: calc(100% - 32px);
        width: 32px;
        height: 32px;
      }
    }
</style>