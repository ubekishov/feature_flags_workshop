import {
  Event as FFEvent,
  initialize
} from '@harnessio/ff-javascript-client-sdk'

let key: string = localStorage.getItem('key') ?? 'b1c11289-d7fc-4702-b8ec-632efcc1bdc7';

const ffClient = initialize(key, {
  name: 'Test user',
  identifier: 'test_user'
})

const bodyEl = document.querySelector('body') as HTMLBodyElement

function setDarkMode(isDark: boolean): void {
  if (isDark) {
    bodyEl.classList.add('darkMode')
  } else {
    bodyEl.classList.remove('darkMode')
  }
}

ffClient.on(FFEvent.READY, () => {
  console.log('The FF SDK is ready')
})

ffClient.on(FFEvent.CHANGED, ({ flag }) => {
  if (flag === 'dark_mode') {
    setDarkMode(!!ffClient.variation(flag, false))
  }
})